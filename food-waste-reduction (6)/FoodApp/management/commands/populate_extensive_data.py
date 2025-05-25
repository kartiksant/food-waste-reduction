from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from FoodApp.models import FoodCategory, FoodItem, DonationRequest, MealPlan, Notification
from datetime import datetime, timedelta
from django.utils import timezone
import random

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate the database with extensive food data and realistic scenarios'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('🌱 Populating database with extensive food data...'))
        
        # Ensure we have categories first
        self.create_categories()
        
        # Ensure we have users
        self.create_users()
        
        # Create extensive food items
        self.create_extensive_food_items()
        
        # Create realistic donation scenarios
        self.create_donation_scenarios()
        
        # Create meal plans
        self.create_meal_plans()
        
        # Create notifications
        self.create_notifications()
        
        self.stdout.write(self.style.SUCCESS('✅ Database populated successfully!'))

    def create_categories(self):
        """Ensure all food categories exist"""
        categories_data = [
            {'name': 'Fruits', 'icon': '🍎', 'description': 'Fresh fruits and berries'},
            {'name': 'Vegetables', 'icon': '🥕', 'description': 'Fresh vegetables and greens'},
            {'name': 'Dairy', 'icon': '🥛', 'description': 'Milk, cheese, yogurt products'},
            {'name': 'Meat & Poultry', 'icon': '🥩', 'description': 'Fresh and frozen meat products'},
            {'name': 'Seafood', 'icon': '🐟', 'description': 'Fresh and frozen fish and seafood'},
            {'name': 'Bakery', 'icon': '🍞', 'description': 'Bread, pastries, baked goods'},
            {'name': 'Prepared Foods', 'icon': '🍽️', 'description': 'Ready-to-eat meals'},
            {'name': 'Pantry Items', 'icon': '🥫', 'description': 'Canned goods and dry ingredients'},
            {'name': 'Beverages', 'icon': '🥤', 'description': 'Drinks and beverages'},
            {'name': 'Frozen Foods', 'icon': '🧊', 'description': 'Frozen meals and ingredients'},
            {'name': 'Snacks', 'icon': '🍿', 'description': 'Chips, crackers, and snack foods'},
            {'name': 'Desserts', 'icon': '🍰', 'description': 'Cakes, cookies, and sweet treats'}
        ]

        for cat_data in categories_data:
            category, created = FoodCategory.objects.get_or_create(
                name=cat_data['name'],
                defaults=cat_data
            )
            if created:
                self.stdout.write(f'📂 Created category: {category.name}')

    def create_users(self):
        """Ensure we have all necessary users"""
        # Create admin if doesn't exist
        admin_user, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@foodsaver.com',
                'role': 'admin',
                'is_staff': True,
                'is_superuser': True,
                'first_name': 'Admin',
                'last_name': 'User'
            }
        )
        if created:
            admin_user.set_password('admin123')
            admin_user.save()

        # Create contributors
        contributors_data = [
            {
                'username': 'greenbistro',
                'email': 'contact@greenbistro.com',
                'password': 'restaurant123',
                'organization_name': 'Green Bistro Restaurant',
                'address': '123 Main Street, Downtown District',
                'phone': '+1-555-0123',
                'first_name': 'Maria',
                'last_name': 'Rodriguez'
            },
            {
                'username': 'freshmarket',
                'email': 'manager@freshmarket.com',
                'password': 'grocery123',
                'organization_name': 'Fresh Market Grocery',
                'address': '456 Oak Avenue, Midtown Plaza',
                'phone': '+1-555-0456',
                'first_name': 'David',
                'last_name': 'Chen'
            },
            {
                'username': 'organicfarm',
                'email': 'harvest@organicfarm.com',
                'password': 'farm123',
                'organization_name': 'Sunny Organic Farm',
                'address': '789 Rural Route 1, Countryside',
                'phone': '+1-555-0789',
                'first_name': 'Emma',
                'last_name': 'Thompson'
            },
            {
                'username': 'citybakery',
                'email': 'orders@citybakery.com',
                'password': 'bakery123',
                'organization_name': 'City Center Bakery',
                'address': '321 Baker Street, Arts District',
                'phone': '+1-555-0321',
                'first_name': 'Pierre',
                'last_name': 'Dubois'
            }
        ]

        for data in contributors_data:
            user, created = User.objects.get_or_create(
                username=data['username'],
                defaults={
                    'email': data['email'],
                    'role': 'contributor',
                    'organization_name': data['organization_name'],
                    'address': data['address'],
                    'phone': data['phone'],
                    'first_name': data['first_name'],
                    'last_name': data['last_name'],
                    'is_verified': True
                }
            )
            if created:
                user.set_password(data['password'])
                user.save()

        # Create recipients
        recipients_data = [
            {
                'username': 'cityfoodbank',
                'email': 'donations@cityfoodbank.org',
                'password': 'foodbank123',
                'organization_name': 'City Food Bank',
                'address': '555 Charity Lane, Southside',
                'phone': '+1-555-0555',
                'first_name': 'Jennifer',
                'last_name': 'Williams'
            },
            {
                'username': 'hopeshelter',
                'email': 'help@hopeshelter.org',
                'password': 'shelter123',
                'organization_name': 'Hope Community Shelter',
                'address': '777 Hope Street, Eastside',
                'phone': '+1-555-0777',
                'first_name': 'Robert',
                'last_name': 'Johnson'
            }
        ]

        for data in recipients_data:
            user, created = User.objects.get_or_create(
                username=data['username'],
                defaults={
                    'email': data['email'],
                    'role': 'recipient',
                    'organization_name': data['organization_name'],
                    'address': data['address'],
                    'phone': data['phone'],
                    'first_name': data['first_name'],
                    'last_name': data['last_name'],
                    'is_verified': True
                }
            )
            if created:
                user.set_password(data['password'])
                user.save()

        # Create individuals
        individuals_data = [
            {
                'username': 'johnsmith',
                'email': 'john.smith@email.com',
                'password': 'individual123',
                'first_name': 'John',
                'last_name': 'Smith',
                'address': '123 Residential Ave, Suburbs',
                'phone': '+1-555-1234'
            },
            {
                'username': 'maryjohnson',
                'email': 'mary.johnson@email.com',
                'password': 'individual123',
                'first_name': 'Mary',
                'last_name': 'Johnson',
                'address': '456 Family Drive, Suburbs',
                'phone': '+1-555-4567'
            }
        ]

        for data in individuals_data:
            user, created = User.objects.get_or_create(
                username=data['username'],
                defaults={
                    'email': data['email'],
                    'role': 'individual',
                    'first_name': data['first_name'],
                    'last_name': data['last_name'],
                    'address': data['address'],
                    'phone': data['phone']
                }
            )
            if created:
                user.set_password(data['password'])
                user.save()

    def create_extensive_food_items(self):
        """Create extensive food items across all categories"""
        
        # Get users and categories
        contributors = User.objects.filter(role='contributor')
        categories = {cat.name: cat for cat in FoodCategory.objects.all()}
        
        if not contributors.exists():
            self.stdout.write(self.style.WARNING('No contributors found. Creating basic contributor...'))
            return

        # Extensive food items data
        food_items_data = [
            # FRUITS
            {
                'contributor': 'greenbistro',
                'name': 'Organic Apple Medley',
                'category': 'Fruits',
                'description': 'Mix of red and green organic apples. Some have minor bruises but are perfect for cooking or eating fresh.',
                'quantity': 25,
                'unit': 'pieces',
                'expiry_hours': 120,
                'pickup_location': 'Green Bistro Restaurant, 123 Main Street (back entrance)',
                'special_instructions': 'Apples are in crates. Some bruising but still fresh and delicious.'
            },
            {
                'contributor': 'freshmarket',
                'name': 'Overripe Banana Bundle',
                'category': 'Fruits',
                'description': 'Very ripe bananas with brown spots. Perfect for banana bread, smoothies, or baking.',
                'quantity': 40,
                'unit': 'pieces',
                'expiry_hours': 48,
                'pickup_location': 'Fresh Market Grocery, 456 Oak Avenue (loading dock)',
                'special_instructions': 'Bananas are very ripe but excellent for baking. Available during business hours.'
            },
            {
                'contributor': 'organicfarm',
                'name': 'Seasonal Berry Mix',
                'category': 'Fruits',
                'description': 'Fresh strawberries and blueberries. Some are very ripe and need to be used quickly.',
                'quantity': 8,
                'unit': 'kg',
                'expiry_hours': 72,
                'pickup_location': 'Sunny Organic Farm, 789 Rural Route 1 (farm stand)',
                'special_instructions': 'Berries are at peak ripeness. Use quickly or freeze for preservation.'
            },

            # VEGETABLES
            {
                'contributor': 'greenbistro',
                'name': 'Fresh Garden Salad Mix',
                'category': 'Vegetables',
                'description': 'Mixed greens including lettuce, spinach, and arugula. Pre-washed and ready to use.',
                'quantity': 12,
                'unit': 'portions',
                'expiry_hours': 24,
                'pickup_location': 'Green Bistro Restaurant, 123 Main Street (back entrance)',
                'special_instructions': 'Salads are in individual containers. Keep refrigerated.'
            },
            {
                'contributor': 'organicfarm',
                'name': 'Root Vegetable Collection',
                'category': 'Vegetables',
                'description': 'Carrots, potatoes, and onions with minor cosmetic imperfections. Great for soups and stews.',
                'quantity': 15,
                'unit': 'kg',
                'expiry_hours': 336,  # 2 weeks
                'pickup_location': 'Sunny Organic Farm, 789 Rural Route 1 (farm stand)',
                'special_instructions': 'Vegetables have cosmetic imperfections but are fresh and nutritious.'
            },
            {
                'contributor': 'freshmarket',
                'name': 'Bell Pepper Variety Pack',
                'category': 'Vegetables',
                'description': 'Red, yellow, and green bell peppers. Some are slightly soft but perfect for cooking.',
                'quantity': 20,
                'unit': 'pieces',
                'expiry_hours': 96,
                'pickup_location': 'Fresh Market Grocery, 456 Oak Avenue (loading dock)',
                'special_instructions': 'Peppers are slightly soft but great for roasting or stir-frying.'
            },

            # BAKERY
            {
                'contributor': 'citybakery',
                'name': 'Artisan Bread Assortment',
                'category': 'Bakery',
                'description': 'Sourdough, whole wheat, and rye loaves from yesterday. Perfect for sandwiches or toast.',
                'quantity': 15,
                'unit': 'loaves',
                'expiry_hours': 48,
                'pickup_location': 'City Center Bakery, 321 Baker Street (side entrance)',
                'special_instructions': 'Bread can be sliced on request. Freezes well for longer storage.'
            },
            {
                'contributor': 'citybakery',
                'name': 'Pastry Selection',
                'category': 'Desserts',
                'description': 'Mixed pastries including croissants, muffins, and Danish from yesterday.',
                'quantity': 25,
                'unit': 'pieces',
                'expiry_hours': 36,
                'pickup_location': 'City Center Bakery, 321 Baker Street (side entrance)',
                'special_instructions': 'Pastries are individually wrapped. Can be refreshed in oven.'
            },

            # DAIRY
            {
                'contributor': 'freshmarket',
                'name': 'Dairy Products Mix',
                'category': 'Dairy',
                'description': 'Assorted dairy products including milk, yogurt, and cheese approaching sell-by date.',
                'quantity': 20,
                'unit': 'items',
                'expiry_hours': 72,
                'pickup_location': 'Fresh Market Grocery, 456 Oak Avenue (loading dock)',
                'special_instructions': 'Items are in refrigerated bags. Check individual expiry dates.'
            },

            # PREPARED FOODS
            {
                'contributor': 'greenbistro',
                'name': 'Roasted Vegetable Medley',
                'category': 'Prepared Foods',
                'description': 'Roasted zucchini, bell peppers, and eggplant with herbs. Made fresh today.',
                'quantity': 8,
                'unit': 'portions',
                'expiry_hours': 48,
                'pickup_location': 'Green Bistro Restaurant, 123 Main Street (back entrance)',
                'special_instructions': 'Vegetables are in food-safe containers. Keep refrigerated and reheat.'
            },
            {
                'contributor': 'greenbistro',
                'name': 'Homemade Soup Variety',
                'category': 'Prepared Foods',
                'description': 'Tomato basil and vegetable soups made fresh today. Perfect for immediate consumption.',
                'quantity': 6,
                'unit': 'liters',
                'expiry_hours': 24,
                'pickup_location': 'Green Bistro Restaurant, 123 Main Street (back entrance)',
                'special_instructions': 'Soup is in sealed containers. Keep refrigerated and reheat before serving.'
            },

            # PANTRY ITEMS
            {
                'contributor': 'freshmarket',
                'name': 'Canned Goods Clearance',
                'category': 'Pantry Items',
                'description': 'Assorted canned vegetables, beans, and soups. Labels may be damaged but contents are perfect.',
                'quantity': 50,
                'unit': 'cans',
                'expiry_hours': 8760,  # 1 year
                'pickup_location': 'Fresh Market Grocery, 456 Oak Avenue (loading dock)',
                'special_instructions': 'Cans have damaged labels but are not expired. Long shelf life.'
            },

            # MEAT & POULTRY
            {
                'contributor': 'freshmarket',
                'name': 'Fresh Chicken Portions',
                'category': 'Meat & Poultry',
                'description': 'Fresh chicken breasts and thighs approaching sell-by date but still perfectly fresh.',
                'quantity': 10,
                'unit': 'kg',
                'expiry_hours': 48,
                'pickup_location': 'Fresh Market Grocery, 456 Oak Avenue (loading dock)',
                'special_instructions': 'Meat is vacuum-sealed and refrigerated. Use within 2 days or freeze.'
            },

            # BEVERAGES
            {
                'contributor': 'freshmarket',
                'name': 'Juice and Beverage Mix',
                'category': 'Beverages',
                'description': 'Assorted fruit juices and beverages approaching expiry but still fresh.',
                'quantity': 30,
                'unit': 'bottles',
                'expiry_hours': 168,  # 1 week
                'pickup_location': 'Fresh Market Grocery, 456 Oak Avenue (loading dock)',
                'special_instructions': 'Beverages are in cases. Check individual expiry dates.'
            },

            # FROZEN FOODS
            {
                'contributor': 'freshmarket',
                'name': 'Frozen Vegetable Medley',
                'category': 'Frozen Foods',
                'description': 'Mixed frozen vegetables in damaged packaging but contents are perfectly fine.',
                'quantity': 15,
                'unit': 'bags',
                'expiry_hours': 2160,  # 3 months
                'pickup_location': 'Fresh Market Grocery, 456 Oak Avenue (loading dock)',
                'special_instructions': 'Packaging is damaged but vegetables are still frozen and fresh.'
            },

            # SNACKS
            {
                'contributor': 'freshmarket',
                'name': 'Snack Food Variety',
                'category': 'Snacks',
                'description': 'Chips, crackers, and snack foods with damaged packaging but contents intact.',
                'quantity': 25,
                'unit': 'packages',
                'expiry_hours': 720,  # 1 month
                'pickup_location': 'Fresh Market Grocery, 456 Oak Avenue (loading dock)',
                'special_instructions': 'Packaging is damaged but snacks are fresh and sealed inside.'
            }
        ]

        # Create food items
        for item_data in food_items_data:
            try:
                contributor = User.objects.get(username=item_data['contributor'])
                category = categories[item_data['category']]
                
                expiry_date = timezone.now() + timedelta(hours=item_data['expiry_hours'])
                
                food_item, created = FoodItem.objects.get_or_create(
                    contributor=contributor,
                    name=item_data['name'],
                    defaults={
                        'category': category,
                        'description': item_data['description'],
                        'quantity': item_data['quantity'],
                        'unit': item_data['unit'],
                        'expiry_date': expiry_date,
                        'pickup_location': item_data['pickup_location'],
                        'special_instructions': item_data['special_instructions'],
                        'status': 'available'
                    }
                )
                
                if created:
                    self.stdout.write(f'🍎 Created food item: {food_item.name}')
                    
            except User.DoesNotExist:
                self.stdout.write(f'⚠️ Contributor {item_data["contributor"]} not found')
            except Exception as e:
                self.stdout.write(f'❌ Error creating {item_data["name"]}: {str(e)}')

    def create_donation_scenarios(self):
        """Create realistic donation request scenarios"""
        recipients = User.objects.filter(role='recipient')
        available_items = FoodItem.objects.filter(status='available')[:10]
        
        if not recipients.exists() or not available_items.exists():
            return

        request_messages = [
            "Hello! We serve 200+ meals daily and would love to use this food to help our community. We can pick up anytime that works for you.",
            "Our food bank distributes to 50+ families weekly. This donation would make a huge difference. Thank you for considering us!",
            "We run a community kitchen and this would help us prepare nutritious meals for those in need. We have refrigerated transport available.",
            "Our shelter houses 30 residents and we're always in need of fresh food. We can coordinate pickup at your convenience.",
        ]

        for i, item in enumerate(available_items[:8]):
            recipient = recipients[i % len(recipients)]
            requested_qty = min(item.quantity // 2, random.randint(1, 10))
            pickup_time = timezone.now() + timedelta(hours=random.randint(6, 48))
            
            # Create some approved and some pending requests
            status = 'approved' if i % 3 == 0 else 'pending'
            
            request, created = DonationRequest.objects.get_or_create(
                food_item=item,
                recipient=recipient,
                defaults={
                    'requested_quantity': requested_qty,
                    'message': random.choice(request_messages),
                    'pickup_time': pickup_time,
                    'status': status
                }
            )
            
            if created:
                # Update item status if approved
                if status == 'approved':
                    item.status = 'reserved'
                    item.save()
                
                self.stdout.write(f'📋 Created request: {recipient.organization_name} → {item.name}')

    def create_meal_plans(self):
        """Create sample meal plans"""
        individuals = User.objects.filter(role='individual')
        
        if not individuals.exists():
            return

        meal_plans_data = [
            {
                'title': 'Zero-Waste Vegetable Stir Fry',
                'description': 'A colorful stir fry using leftover vegetables',
                'ingredients': 'Mixed vegetables (2 cups), Rice (1 cup), Soy sauce (2 tbsp), Garlic (2 cloves), Oil (1 tbsp)',
                'instructions': '''1. Heat oil in a large pan
2. Add garlic and cook for 30 seconds
3. Add vegetables and stir-fry for 5-7 minutes
4. Add soy sauce and serve over rice''',
                'servings': 4,
                'prep_time': 15,
                'ai_generated': False
            },
            {
                'title': 'Banana Bread from Overripe Bananas',
                'description': 'Transform brown bananas into delicious bread',
                'ingredients': 'Overripe bananas (3), Flour (2 cups), Sugar (3/4 cup), Butter (1/3 cup), Egg (1)',
                'instructions': '''1. Preheat oven to 350°F
2. Mash bananas in a bowl
3. Mix in butter, sugar, and egg
4. Add flour and mix until combined
5. Bake for 60 minutes''',
                'servings': 8,
                'prep_time': 75,
                'ai_generated': False
            }
        ]

        for i, plan_data in enumerate(meal_plans_data):
            user = individuals[i % len(individuals)]
            plan, created = MealPlan.objects.get_or_create(
                user=user,
                title=plan_data['title'],
                defaults=plan_data
            )
            if created:
                self.stdout.write(f'🍽️ Created meal plan: {plan.title}')

    def create_notifications(self):
        """Create sample notifications"""
        contributors = User.objects.filter(role='contributor')
        recipients = User.objects.filter(role='recipient')
        
        if contributors.exists() and recipients.exists():
            # Create sample notifications
            notifications_data = [
                {
                    'user': contributors.first(),
                    'title': 'New Donation Request',
                    'message': f'{recipients.first().organization_name} has requested your fresh vegetables.',
                    'type': 'donation_request',
                    'is_read': False
                },
                {
                    'user': recipients.first(),
                    'title': 'Donation Request Approved',
                    'message': f'Your request has been approved by {contributors.first().organization_name}.',
                    'type': 'donation_request',
                    'is_read': False
                }
            ]

            for notif_data in notifications_data:
                notification, created = Notification.objects.get_or_create(
                    user=notif_data['user'],
                    title=notif_data['title'],
                    defaults=notif_data
                )
                if created:
                    self.stdout.write(f'🔔 Created notification: {notification.title}')
