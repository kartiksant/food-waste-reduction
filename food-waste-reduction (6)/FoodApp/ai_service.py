"""
AI Service for Food Waste Prediction and Smart Notifications
"""
import google.generativeai as genai
from django.conf import settings
from django.utils import timezone
from datetime import timedelta, datetime
import json
import re
from .models import FoodItem, FoodCategory, DemandPattern, FoodWastePrediction, SmartAlert, Notification, User

# Configure Gemini AI
genai.configure(api_key=settings.GEMINI_API_KEY)

class FoodWasteAI:
    def __init__(self):
        self.model = genai.GenerativeModel('gemini-pro')
    
    def predict_food_waste(self, contributor, food_category, analysis_period='week'):
        """Predict food waste patterns using AI"""
        try:
            # Get historical data
            historical_items = FoodItem.objects.filter(
                contributor=contributor,
                category=food_category,
                created_at__gte=timezone.now() - timedelta(days=90)
            )
            
            # Prepare data for AI analysis
            waste_data = []
            for item in historical_items:
                waste_data.append({
                    'name': item.name,
                    'quantity': item.quantity,
                    'status': item.status,
                    'created_date': item.created_at.strftime('%A'),
                    'expiry_days': item.days_until_expiry()
                })
            
            # Create AI prompt
            prompt = f"""
            Analyze the following food waste data for {contributor.organization_name} in the {food_category.name} category:
            
            Historical Data: {json.dumps(waste_data, indent=2)}
            
            Based on this data, predict:
            1. Which day of the week has highest waste for {food_category.name}
            2. Approximate quantity that might be wasted in the next {analysis_period}
            3. Specific recommendations to reduce waste
            4. Best times to notify potential recipients
            
            Focus on patterns like "Biryani is mostly wasted on Saturdays" and provide actionable insights.
            
            Respond in JSON format:
            {{
                "high_waste_day": "Saturday",
                "predicted_quantity": 15,
                "confidence": 0.85,
                "recommendations": ["suggestion1", "suggestion2"],
                "optimal_notification_times": ["Friday evening", "Saturday morning"],
                "waste_pattern": "detailed analysis"
            }}
            """
            
            response = self.model.generate_content(prompt)
            
            # Parse AI response
            try:
                # Extract JSON from response
                json_match = re.search(r'\{.*\}', response.text, re.DOTALL)
                if json_match:
                    ai_data = json.loads(json_match.group())
                else:
                    # Fallback if JSON parsing fails
                    ai_data = {
                        "high_waste_day": "Saturday",
                        "predicted_quantity": 10,
                        "confidence": 0.7,
                        "recommendations": ["Monitor weekend demand", "Offer early discounts"],
                        "optimal_notification_times": ["Friday evening"],
                        "waste_pattern": response.text
                    }
            except:
                ai_data = {
                    "high_waste_day": "Saturday",
                    "predicted_quantity": 10,
                    "confidence": 0.7,
                    "recommendations": ["Monitor weekend demand"],
                    "optimal_notification_times": ["Friday evening"],
                    "waste_pattern": "Analysis completed"
                }
            
            # Save prediction
            prediction = FoodWastePrediction.objects.create(
                contributor=contributor,
                food_category=food_category,
                predicted_waste_date=timezone.now().date() + timedelta(days=7),
                predicted_quantity=ai_data.get('predicted_quantity', 10),
                confidence_score=ai_data.get('confidence', 0.7),
                historical_pattern=json.dumps(waste_data),
                ai_suggestions=json.dumps(ai_data.get('recommendations', []))
            )
            
            # Create smart alerts for recipients
            self.create_waste_alerts(contributor, food_category, ai_data)
            
            return ai_data
            
        except Exception as e:
            print(f"AI Prediction Error: {str(e)}")
            return {
                "error": "AI prediction temporarily unavailable",
                "predicted_quantity": 5,
                "recommendations": ["Monitor food levels", "Contact recipients early"]
            }
    
    def create_waste_alerts(self, contributor, food_category, ai_data):
        """Create smart alerts for potential recipients"""
        try:
            # Find relevant recipients
            recipients = User.objects.filter(role='recipient', is_active=True)
            
            high_waste_day = ai_data.get('high_waste_day', 'Saturday')
            predicted_quantity = ai_data.get('predicted_quantity', 10)
            
            for recipient in recipients:
                # Create notification
                notification_message = f"""
🤖 AI Prediction Alert: {contributor.organization_name} typically has surplus {food_category.name} on {high_waste_day}s.

📊 Predicted surplus: ~{predicted_quantity} units
📅 Next opportunity: This {high_waste_day}
🎯 Recommendation: Contact them early for best selection

This prediction is based on historical patterns and AI analysis.
                """.strip()
                
                Notification.objects.create(
                    user=recipient,
                    title=f'AI Prediction: {food_category.name} Surplus Expected',
                    message=notification_message,
                    type='ai_prediction'
                )
                
                # Create smart alert
                SmartAlert.objects.create(
                    user=recipient,
                    alert_type='waste_prediction',
                    title=f'Predicted {food_category.name} Surplus',
                    message=f'{contributor.organization_name} likely to have {predicted_quantity} units of {food_category.name} surplus on {high_waste_day}',
                    action_data=json.dumps({
                        'contributor_id': contributor.id,
                        'category_id': food_category.id,
                        'predicted_day': high_waste_day,
                        'quantity': predicted_quantity
                    }),
                    expires_at=timezone.now() + timedelta(days=7)
                )
        
        except Exception as e:
            print(f"Alert Creation Error: {str(e)}")
    
    def generate_smart_meal_plan(self, ingredients, dietary_preferences, servings, waste_context=None):
        """Generate AI meal plan with waste reduction focus"""
        try:
            waste_prompt = ""
            if waste_context:
                waste_prompt = f"\nAdditional context: {waste_context}"
            
            prompt = f"""
            Create a detailed meal plan that reduces food waste using these ingredients: {ingredients}
            
            Requirements:
            - Servings: {servings}
            - Dietary preferences: {dietary_preferences or 'None specified'}
            - Focus on using ALL ingredients efficiently
            - Minimize food waste{waste_prompt}
            
            Provide:
            1. Creative meal title
            2. Brief description focusing on waste reduction
            3. Complete ingredients list with quantities
            4. Step-by-step cooking instructions
            5. Tips for using leftovers
            6. Storage recommendations
            
            Make it practical and waste-conscious.
            """
            
            response = self.model.generate_content(prompt)
            return response.text
            
        except Exception as e:
            print(f"Meal Plan Generation Error: {str(e)}")
            return f"""
            Waste-Reducing Meal Plan
            
            Using: {ingredients}
            Servings: {servings}
            
            Instructions:
            1. Prepare all ingredients: {ingredients}
            2. Cook using your preferred method
            3. Season to taste
            4. Store leftovers properly to avoid waste
            
            This meal plan helps reduce food waste by using all available ingredients efficiently.
            """
    
    def analyze_demand_patterns(self):
        """Analyze demand patterns across the platform"""
        try:
            # Get recent donation data
            from .models import DonationRequest
            recent_requests = DonationRequest.objects.filter(
                created_at__gte=timezone.now() - timedelta(days=30)
            ).select_related('food_item__category')
            
            # Group by category and day of week
            demand_data = {}
            for request in recent_requests:
                category = request.food_item.category.name
                day_of_week = request.created_at.weekday()
                
                if category not in demand_data:
                    demand_data[category] = [0] * 7
                
                demand_data[category][day_of_week] += request.requested_quantity
            
            # Update demand patterns
            for category_name, weekly_demand in demand_data.items():
                try:
                    category = FoodCategory.objects.get(name=category_name)
                    for day, demand in enumerate(weekly_demand):
                        DemandPattern.objects.update_or_create(
                            food_category=category,
                            day_of_week=day,
                            defaults={'typical_demand': demand}
                        )
                except FoodCategory.DoesNotExist:
                    continue
            
            return demand_data
            
        except Exception as e:
            print(f"Demand Analysis Error: {str(e)}")
            return {}
    
    def create_personalized_notifications(self, user):
        """Create personalized notifications based on user behavior"""
        try:
            if user.role == 'recipient':
                # Analyze recipient's request patterns
                recent_requests = user.donation_requests.filter(
                    created_at__gte=timezone.now() - timedelta(days=30)
                )
                
                if recent_requests.exists():
                    # Find preferred categories
                    preferred_categories = {}
                    for request in recent_requests:
                        category = request.food_item.category.name
                        preferred_categories[category] = preferred_categories.get(category, 0) + 1
                    
                    # Find items in preferred categories
                    top_category = max(preferred_categories, key=preferred_categories.get)
                    available_items = FoodItem.objects.filter(
                        category__name=top_category,
                        status='available',
                        expiry_date__gte=timezone.now()
                    )[:3]
                    
                    if available_items:
                        message = f"New {top_category} items available based on your preferences:\n"
                        for item in available_items:
                            message += f"• {item.name} ({item.quantity} {item.unit}) from {item.contributor.organization_name}\n"
                        
                        Notification.objects.create(
                            user=user,
                            title=f'Personalized Alert: {top_category} Available',
                            message=message,
                            type='system'
                        )
            
            elif user.role == 'contributor':
                # Check for items approaching expiry
                expiring_items = user.food_items.filter(
                    status='available',
                    expiry_date__lte=timezone.now() + timedelta(days=1)
                )
                
                if expiring_items.exists():
                    message = f"⚠️ {expiring_items.count()} items expiring soon:\n"
                    for item in expiring_items[:3]:
                        message += f"• {item.name} expires {item.expiry_date.strftime('%m/%d at %H:%M')}\n"
                    message += "\nConsider promoting these items or contacting recipients directly."
                    
                    Notification.objects.create(
                        user=user,
                        title='Urgent: Items Expiring Soon',
                        message=message,
                        type='expiry_alert'
                    )
        
        except Exception as e:
            print(f"Personalized Notification Error: {str(e)}")


# Initialize AI service
ai_service = FoodWasteAI()
