"""
Django views for the Food Waste Reduction Platform
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Sum, Count
from django.utils import timezone
from datetime import timedelta
import json

# AI functionality
try:
    import google.generativeai as genai
    from .ai_service import ai_service
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False
    ai_service = None

from django.conf import settings
from .models import (User, FoodItem, DonationRequest, MealPlan, WasteAnalytics, 
                    Notification, FoodCategory, FoodWastePrediction, SmartAlert)
from .forms import (CustomUserCreationForm, FoodItemForm, DonationRequestForm, 
                   MealPlanForm, AIIngredientForm, WastePredictionForm)


def home(request):
    """Landing page with platform overview"""
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    # Get platform statistics
    total_food_saved = FoodItem.objects.filter(status='donated').aggregate(
        total=Sum('quantity'))['total'] or 0
    total_donations = DonationRequest.objects.filter(status='completed').count()
    active_contributors = User.objects.filter(role='contributor', is_active=True).count()
    
    context = {
        'total_food_saved': total_food_saved,
        'total_donations': total_donations,
        'active_contributors': active_contributors,
    }
    return render(request, 'FoodApp/home.html', context)


def register(request):
    """User registration view"""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def dashboard(request):
    """Role-based dashboard with AI insights"""
    user = request.user
    context = {'user': user}
    
    # Create personalized notifications
    if GEMINI_AVAILABLE and ai_service:
        try:
            ai_service.create_personalized_notifications(user)
        except:
            pass
    
    if user.role == 'admin':
        # Admin dashboard
        context.update({
            'total_users': User.objects.count(),
            'total_food_items': FoodItem.objects.count(),
            'pending_requests': DonationRequest.objects.filter(status='pending').count(),
            'food_saved_today': FoodItem.objects.filter(
                status='donated', 
                updated_at__date=timezone.now().date()
            ).aggregate(total=Sum('quantity'))['total'] or 0,
            'recent_donations': DonationRequest.objects.filter(status='completed')[:5],
            'ai_predictions': FoodWastePrediction.objects.all()[:5],
        })
        return render(request, 'FoodApp/admin_dashboard.html', context)
    
    elif user.role == 'contributor':
        # Restaurant/Grocer dashboard
        my_items = FoodItem.objects.filter(contributor=user)
        expiring_soon = my_items.filter(
            expiry_date__lte=timezone.now() + timedelta(days=2),
            status='available'
        )
        
        # Get AI predictions for this contributor
        predictions = FoodWastePrediction.objects.filter(contributor=user)[:3]
        
        context.update({
            'my_food_items': my_items[:10],
            'expiring_soon': expiring_soon,
            'total_donated': my_items.filter(status='donated').count(),
            'pending_requests': DonationRequest.objects.filter(
                food_item__contributor=user, 
                status='pending'
            ),
            'ai_predictions': predictions,
        })
        return render(request, 'FoodApp/contributor_dashboard.html', context)
    
    elif user.role == 'recipient':
        # Charity/Food Bank dashboard
        my_requests = DonationRequest.objects.filter(recipient=user)
        available_food = FoodItem.objects.filter(status='available')[:10]
        
        # Get smart alerts for this recipient
        smart_alerts = SmartAlert.objects.filter(user=user, is_active=True)[:3]
        
        context.update({
            'my_requests': my_requests[:10],
            'available_food': available_food,
            'completed_donations': my_requests.filter(status='completed').count(),
            'pending_requests': my_requests.filter(status='pending').count(),
            'smart_alerts': smart_alerts,
        })
        return render(request, 'FoodApp/recipient_dashboard.html', context)
    
    else:
        # Individual dashboard
        my_meal_plans = MealPlan.objects.filter(user=user)[:5]
        nearby_food = FoodItem.objects.filter(status='available')[:8]
        
        context.update({
            'my_meal_plans': my_meal_plans,
            'nearby_food': nearby_food,
            'total_meal_plans': my_meal_plans.count(),
        })
        return render(request, 'FoodApp/individual_dashboard.html', context)


@login_required
def add_food_item(request):
    """Add new food item (Contributors only)"""
    if request.user.role != 'contributor':
        messages.error(request, 'Only contributors can add food items.')
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = FoodItemForm(request.POST, request.FILES)
        if form.is_valid():
            food_item = form.save(commit=False)
            food_item.contributor = request.user
            food_item.save()
            messages.success(request, 'Food item added successfully!')
            return redirect('my_food_items')
        else:
            messages.error(request, 'Please correct the errors in the form.')
    else:
        form = FoodItemForm()
    
    return render(request, 'FoodApp/add_food_item.html', {'form': form})


@login_required
def my_food_items(request):
    """View contributor's food items"""
    if request.user.role != 'contributor':
        return redirect('dashboard')
    
    items = FoodItem.objects.filter(contributor=request.user).order_by('-created_at')
    return render(request, 'FoodApp/my_food_items.html', {'items': items})


@login_required
def available_food(request):
    """Browse available food items"""
    items = FoodItem.objects.filter(status='available').order_by('expiry_date')
    
    # Filter by category if specified
    category_id = request.GET.get('category')
    if category_id:
        items = items.filter(category_id=category_id)
    
    # Filter by urgency
    urgency = request.GET.get('urgency')
    if urgency:
        items = items.filter(urgency=urgency)
    
    categories = FoodCategory.objects.all()
    
    context = {
        'items': items,
        'categories': categories,
        'selected_category': category_id,
        'selected_urgency': urgency,
    }
    return render(request, 'FoodApp/available_food.html', context)


@login_required
def request_donation(request, food_item_id):
    """Request a food donation"""
    food_item = get_object_or_404(FoodItem, id=food_item_id, status='available')
    
    if request.user.role not in ['recipient', 'individual']:
        messages.error(request, 'Only recipients and individuals can request donations.')
        return redirect('available_food')
    
    if request.method == 'POST':
        form = DonationRequestForm(request.POST)
        if form.is_valid():
            donation_request = form.save(commit=False)
            donation_request.food_item = food_item
            donation_request.recipient = request.user
            donation_request.save()
            
            # Create notification for contributor
            try:
                Notification.objects.create(
                    user=food_item.contributor,
                    title='New Donation Request',
                    message=f'{request.user.organization_name or request.user.username} has requested {donation_request.requested_quantity} {food_item.unit} of {food_item.name}',
                    type='donation_request'
                )
            except:
                pass  # Continue even if notification fails
            
            messages.success(request, 'Donation request submitted successfully!')
            return redirect('my_requests')
        else:
            messages.error(request, 'Please correct the errors in the form.')
    else:
        form = DonationRequestForm()
    
    return render(request, 'FoodApp/request_donation.html', {
        'form': form, 
        'food_item': food_item
    })


@login_required
def my_requests(request):
    """View user's donation requests"""
    requests = DonationRequest.objects.filter(recipient=request.user).order_by('-created_at')
    return render(request, 'FoodApp/my_requests.html', {'requests': requests})


@login_required
def manage_requests(request):
    """Manage incoming donation requests (Contributors only)"""
    if request.user.role != 'contributor':
        return redirect('dashboard')
    
    requests = DonationRequest.objects.filter(
        food_item__contributor=request.user
    ).order_by('-created_at')
    
    return render(request, 'FoodApp/manage_requests.html', {'requests': requests})


@login_required
def approve_request(request, request_id):
    """Approve or reject a donation request"""
    donation_request = get_object_or_404(
        DonationRequest, 
        id=request_id, 
        food_item__contributor=request.user
    )
    
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'approve':
            donation_request.status = 'approved'
            donation_request.food_item.status = 'reserved'
            donation_request.food_item.save()
            
            # Create notification for recipient
            try:
                Notification.objects.create(
                    user=donation_request.recipient,
                    title='Donation Request Approved',
                    message=f'Your request for {donation_request.food_item.name} has been approved!',
                    type='donation_request'
                )
            except:
                pass
            
            messages.success(request, 'Donation request approved!')
        
        elif action == 'reject':
            donation_request.status = 'cancelled'
            messages.info(request, 'Donation request rejected.')
        
        donation_request.save()
    
    return redirect('manage_requests')


@login_required
def ai_meal_planner(request):
    """AI-powered meal planning with waste reduction focus"""
    if request.method == 'POST':
        form = AIIngredientForm(request.POST)
        if form.is_valid():
            ingredients = form.cleaned_data['ingredients']
            dietary_preferences = form.cleaned_data['dietary_preferences']
            servings = form.cleaned_data['servings']
            
            # Create basic meal plan (works with or without AI)
            title = f"Meal Plan with {ingredients.split(',')[0].strip()}"
            description = f"Waste-reducing meal for {servings} servings"
            instructions = f"""
1. Prepare all ingredients: {ingredients}
2. Clean and chop vegetables as needed
3. Cook according to your preferred method
4. Season with salt, pepper, and herbs to taste
5. Store leftovers properly to avoid waste
6. Serve hot and enjoy!

Dietary preferences: {dietary_preferences or 'None specified'}
"""
            
            # Try to use AI if available
            if GEMINI_AVAILABLE and ai_service:
                try:
                    # Check for nearby expiring food to include in context
                    expiring_food = FoodItem.objects.filter(
                        status='available',
                        expiry_date__lte=timezone.now() + timedelta(days=2)
                    )[:3]
                    
                    waste_context = ""
                    if expiring_food.exists():
                        waste_context = f"Consider incorporating these expiring items: {', '.join([item.name for item in expiring_food])}"
                    
                    ai_response = ai_service.generate_smart_meal_plan(
                        ingredients, dietary_preferences, servings, waste_context
                    )
                    
                    # Parse AI response for title and instructions
                    lines = ai_response.split('\n')
                    for line in lines[:5]:
                        if line.strip() and not line.startswith('#') and len(line) < 100:
                            title = line.strip()
                            break
                    
                    instructions = ai_response
                    description = f"AI-generated waste-reducing meal plan for {servings} servings"
                    
                except Exception as e:
                    messages.warning(request, 'AI is temporarily unavailable. Created a basic meal plan instead.')
            
            # Save the meal plan
            meal_plan = MealPlan.objects.create(
                user=request.user,
                title=title,
                description=description,
                ingredients=ingredients,
                instructions=instructions,
                servings=servings,
                prep_time=30,
                ai_generated=GEMINI_AVAILABLE and ai_service is not None
            )
            
            messages.success(request, 'Meal plan created successfully!')
            return redirect('meal_plan_detail', meal_plan.id)
    else:
        form = AIIngredientForm()
    
    return render(request, 'FoodApp/ai_meal_planner.html', {'form': form})


@login_required
def waste_prediction(request):
    """AI-powered waste prediction for contributors"""
    if request.user.role != 'contributor':
        messages.error(request, 'Only contributors can access waste predictions.')
        return redirect('dashboard')
    
    predictions = []
    
    if request.method == 'POST':
        form = WastePredictionForm(request.POST)
        if form.is_valid() and GEMINI_AVAILABLE and ai_service:
            try:
                food_category = form.cleaned_data['food_type']
                analysis_period = form.cleaned_data['analysis_period']
                
                # Generate AI prediction
                prediction_data = ai_service.predict_food_waste(
                    request.user, food_category, analysis_period
                )
                
                messages.success(request, f'AI analysis completed for {food_category.name}!')
                
                # Get updated predictions
                predictions = FoodWastePrediction.objects.filter(
                    contributor=request.user
                ).order_by('-created_at')[:5]
                
            except Exception as e:
                messages.error(request, 'AI prediction temporarily unavailable.')
    else:
        form = WastePredictionForm()
        predictions = FoodWastePrediction.objects.filter(
            contributor=request.user
        ).order_by('-created_at')[:5]
    
    context = {
        'form': form,
        'predictions': predictions,
        'ai_available': GEMINI_AVAILABLE and ai_service is not None
    }
    
    return render(request, 'FoodApp/waste_prediction.html', context)


@login_required
def meal_plans(request):
    """View user's meal plans"""
    plans = MealPlan.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'FoodApp/meal_plans.html', {'plans': plans})


@login_required
def meal_plan_detail(request, plan_id):
    """View meal plan details"""
    plan = get_object_or_404(MealPlan, id=plan_id, user=request.user)
    return render(request, 'FoodApp/meal_plan_detail.html', {'plan': plan})


@login_required
def analytics(request):
    """Analytics dashboard"""
    user = request.user
    
    # Calculate user-specific analytics
    if user.role == 'contributor':
        donated_items = FoodItem.objects.filter(contributor=user, status='donated')
        total_food_saved = donated_items.aggregate(total=Sum('quantity'))['total'] or 0
        total_donations = donated_items.count()
        
        # Also count reserved items as they're in the donation process
        reserved_items = FoodItem.objects.filter(contributor=user, status='reserved')
        total_food_saved += reserved_items.aggregate(total=Sum('quantity'))['total'] or 0
        total_donations += reserved_items.count()
        
        co2_reduced = float(total_food_saved) * 2.5
        money_saved = float(total_food_saved) * 5
        
    elif user.role == 'recipient':
        received_donations = DonationRequest.objects.filter(recipient=user, status__in=['completed', 'approved'])
        total_food_received = sum([req.requested_quantity for req in received_donations])
        total_donations = received_donations.count()
        co2_reduced = float(total_food_received) * 2.5
        money_saved = float(total_food_received) * 5
        total_food_saved = total_food_received
        
    else:
        # For individuals and admins, show platform-wide stats
        all_donated_items = FoodItem.objects.filter(status__in=['donated', 'reserved'])
        total_food_saved = all_donated_items.aggregate(total=Sum('quantity'))['total'] or 0
        total_donations = DonationRequest.objects.filter(status__in=['completed', 'approved']).count()
        co2_reduced = float(total_food_saved) * 2.5
        money_saved = float(total_food_saved) * 5
    
    # Global platform statistics
    global_stats = {
        'total_users': User.objects.count(),
        'total_food_saved': FoodItem.objects.filter(status__in=['donated', 'reserved']).aggregate(
            total=Sum('quantity'))['total'] or 0,
        'total_donations': DonationRequest.objects.filter(status__in=['completed', 'approved']).count(),
        'active_contributors': User.objects.filter(role='contributor', is_active=True).count(),
    }
    
    context = {
        'total_food_saved': int(total_food_saved),
        'total_donations': total_donations,
        'co2_reduced': round(co2_reduced, 2),
        'money_saved': round(money_saved, 2),
        'global_stats': global_stats,
    }
    
    return render(request, 'FoodApp/analytics.html', context)


@login_required
def notifications(request):
    """View user notifications"""
    user_notifications = Notification.objects.filter(user=request.user)
    
    # Mark as read if requested
    if request.GET.get('mark_read'):
        user_notifications.update(is_read=True)
        return redirect('notifications')
    
    return render(request, 'FoodApp/notifications.html', {
        'notifications': user_notifications
    })


def api_food_items(request):
    """API endpoint for food items"""
    items = FoodItem.objects.filter(status='available')
    
    data = []
    for item in items:
        data.append({
            'id': item.id,
            'name': item.name,
            'category': item.category.name,
            'quantity': item.quantity,
            'unit': item.unit,
            'expiry_date': item.expiry_date.isoformat(),
            'urgency': item.urgency,
            'contributor': item.contributor.organization_name or item.contributor.username,
        })
    
    return JsonResponse({'items': data})
