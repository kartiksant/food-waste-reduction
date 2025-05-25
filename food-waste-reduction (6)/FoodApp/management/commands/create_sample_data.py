from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from FoodApp.models import FoodCategory, FoodItem, DonationRequest, MealPlan, Notification
from datetime import datetime, timedelta
from django.utils import timezone
import random

User = get_user_model()

class Command(BaseCommand):
    help = 'Create comprehensive sample data for the FoodApp'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('🌱 Creating comprehensive sample data...'))
        
        # Clear existing data (optional - comment out if you want to keep existing data)
        self.stdout.write('🧹 Clearing existing sample data...')
        User.objects.filter(username__in=[
            'admin', 'greenbistro', 'freshmarket', 'organicfarm', 'citybakery',
            'cityfoodbank', 'hopeshelter', 'communitykitchen', 'seniorcare',
            'johnsmith', 'maryjohnson', 'sarahwilson', 'mikebrown'
        ]).delete()
        
        # Create admin user
        admin_user = User.objects.create_user(
            username='admin',
            email='admin@foodsaver.com',
            password='admin123',
            role='admin',
            is_staff=True,
            is_superuser=True,
            first_name='Admin',
            last_name='User'
        )
        self.stdout.write('👑 Created admin: admin/admin123')

        # Create Contributors (Restaurants, Groceries, Farms)
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

        contributors = []
        for data in contributors_data:
            user = User.objects.create_user(
                username=data['username'],
                email=data['email'],
                password=data['password'],
                role='contributor',
                organization_name=data['organization_name'],
                address=data['address'],
                phone=data['phone'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                is_verified=True
            )
            contributors.append(user)
            self.stdout.write(f'🏪 Created contributor: {data["username"]}/{data["password"]}')

        # Create Recipients (Food Banks, Shelters, Community Centers)
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
            },
            {
                'username': 'communitykitchen',
                'email': 'meals@communitykitchen.org',
                'password': 'kitchen123',
                'organization_name': 'Community Kitchen Network',
                'address': '999 Service Avenue, Central',
                'phone': '+1-555-0999',
                'first_name': 'Lisa',
                'last_name': 'Anderson'
            },
            {
                'username': 'seniorcare',
                'email': 'nutrition@seniorcare.org',
                'password': 'senior123',
                'organization_name': 'Senior Care Nutrition Program',
                'address': '111 Elder Way, Westside',
                'phone': '+1-555-0111',
                'first_name': 'Michael',
                'last_name': 'Davis'
            }
        ]

        recipients = []
        for data in recipients_data:
            user = User.objects.create_user(
                username=data['username'],
                email=data['email'],
                password=data['password'],
                role='recipient',
                organization_name=data['organization_name'],
                address=data['address'],
                phone=data['phone'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                is_verified=True
            )
            recipients.append(user)
            self.stdout.write(f'🏦 Created recipient: {data["username"]}/{data["password"]}')

        # Create Individual Users
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
            },
            {
                'username': 'sarahwilson',
                'email': 'sarah.wilson@email.com',
                'password': 'individual123',
                'first_name': 'Sarah',
                'last_name': 'Wilson',
                'address': '789 Green Street, Eco Village',
                'phone': '+1-555-7890'
            },
            {
                'username': 'mikebrown',
                'email': 'mike.brown@email.com',
                'password': 'individual123',
                'first_name': 'Mike',
                'last_name': 'Brown',
                'address': '321 Urban Loft, Downtown',
                'phone': '+1-555-3210'
            }
        ]

        individuals = []
        for data in individuals_data:
            user = User.objects.create_user(
                username=data['username'],
                email=data['email'],
                password=data['password'],
                role='individual',
                first_name=data['first_name'],
                last_name=data['last_name'],
                address=data['address'],
                phone=data['phone']
            )
            individuals.append(user)
            self.stdout.write(f'👤 Created individual: {data["username"]}/{data["password"]}')

        # Create comprehensive food categories
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

        categories = {}
        for cat_data in categories_data:
            category, created = FoodCategory.objects.get_or_create(
                name=cat_data['name'],
                defaults=cat_data
            )
            categories[cat_data['name']] = category
            if created:
                self.stdout.write(f'📂 Created category: {category.name}')

        # Create extensive food items with realistic data
        food_items_data = [
            # Green Bistro Restaurant items
            {
                'contributor': contributors[0],  # Green Bistro
                'name': 'Gourmet Caesar Salad Mix',
                'category': categories['Vegetables'],
                'description': 'Pre-made Caesar salad with romaine lettuce, croutons, and parmesan. Made fresh this morning but approaching end of service.',
                'quantity': 12,
                'unit': 'portions',
                'expiry_hours': 8,
                'pickup_location': 'Green Bistro Restaurant, 123 Main Street (kitchen back door)',
                'special_instructions': 'Salads are in individual containers. Dressing packets included. Best consumed within 8 hours.'
            },
            {
                'contributor': contributors[0],
                'name': 'Artisan Sourdough Bread',
                'category': categories['Bakery'],
                'description': 'Fresh sourdough loaves baked this morning. Slightly over-baked but perfect for toast or bread pudding.',
                'quantity': 8,
                'unit': 'loaves',
                'expiry_hours': 24,
                'pickup_location': 'Green Bistro Restaurant, 123 Main Street (kitchen back door)',
                'special_instructions': 'Bread is wrapped in paper bags. Can be frozen for longer storage.'
            },
            {
                'contributor': contributors[0],
                'name': 'Roasted Vegetable Medley',
                'category': categories['Prepared Foods'],
                'description': 'Roasted zucchini, bell peppers, and eggplant with herbs. Prepared for tonight\'s service but we made too much.',
                'quantity': 5,
                'unit': 'kg',
                'expiry_hours': 48,
                'pickup_location': 'Green Bistro Restaurant, 123 Main Street (kitchen back door)',
                'special_instructions': 'Vegetables are in food-safe containers. Keep refrigerated and reheat before serving.'
            },
            {
                'contributor': contributors[0],
                'name': 'Fresh Herb Collection',
                'category': categories['Vegetables'],
                'description': 'Assorted fresh herbs: basil, parsley, cilantro, and thyme. Slightly wilted but still aromatic and flavorful.',
                'quantity': 2,
                'unit': 'bunches',
                'expiry_hours': 72,
                'pickup_location': 'Green Bistro Restaurant, 123 Main Street (kitchen back door)',
                'special_instructions': 'Herbs are in water containers. Use quickly or dry for preservation.'
            },

            # Fresh Market Grocery items
            {
                'contributor': contributors[1],  # Fresh Market
                'name': 'Overripe Banana Bundle',
                'category': categories['Fruits'],
                'description': 'Very ripe bananas with brown spots. Perfect for banana bread, smoothies, or baking. Sweet and soft.',
                'quantity': 50,
                'unit': 'pieces',
                'expiry_hours': 48,
                'pickup_location': 'Fresh Market Grocery, 456 Oak Avenue (loading dock, ask for manager)',
                'special_instructions': 'Bananas are very ripe but excellent for baking. Available during business hours.'
            },
            {
                'contributor': contributors[1],
                'name': 'Dairy Variety Pack',
                'category': categories['Dairy'],
                'description': 'Mixed dairy products: milk, yogurt, cheese approaching sell-by date but still fresh and safe.',
                'quantity': 25,
                'unit': 'items',
                'expiry_hours': 72,
                'pickup_location': 'Fresh Market Grocery, 456 Oak Avenue (loading dock, ask for manager)',
                'special_instructions': 'Items are in refrigerated bags. Check individual expiry dates - all still good for 2-3 days.'
            },
            {
                'contributor': contributors[1],
                'name': 'Cosmetically Imperfect Apples',
                'category': categories['Fruits'],
                'description': 'Red and green apples with minor bruises and blemishes. Taste is unaffected, great for cooking or juice.',
                'quantity': 30,
                'unit': 'kg',
                'expiry_hours': 168,  # 1 week
                'pickup_location': 'Fresh Market Grocery, 456 Oak Avenue (loading dock, ask for manager)',
                'special_instructions': 'Apples have cosmetic imperfections only. Perfect for pies, sauce, or eating fresh.'
            },
            {
                'contributor': contributors[1],
                'name': 'Canned Goods Clearance',
                'category': categories['Pantry Items'],
                'description': 'Assorted canned vegetables, beans, and soups. Labels may be damaged but contents are perfect.',
                'quantity': 75,
                'unit': 'cans',
                'expiry_hours': 8760,  # 1 year
                'pickup_location': 'Fresh Market Grocery, 456 Oak Avenue (loading dock, ask for manager)',
                'special_instructions': 'Cans have damaged labels but are not expired. Long shelf life remaining.'
            },

            # Sunny Organic Farm items
            {
                'contributor': contributors[2],  # Organic Farm
                'name': 'Farm Fresh Carrots',
                'category': categories['Vegetables'],
                'description': 'Organic carrots with soil still attached. Various sizes, some curved or split but perfectly fresh.',
                'quantity': 20,
                'unit': 'kg',
                'expiry_hours': 336,  # 2 weeks
                'pickup_location': 'Sunny Organic Farm, 789 Rural Route 1 (farm stand)',
                'special_instructions': 'Carrots need washing. Store in cool, dry place. Great for soups, stews, or raw eating.'
            },
            {
                'contributor': contributors[2],
                'name': 'Mixed Seasonal Vegetables',
                'category': categories['Vegetables'],
                'description': 'Seasonal mix of zucchini, tomatoes, and peppers. Some overripe but excellent for cooking.',
                'quantity': 15,
                'unit': 'kg',
                'expiry_hours': 120,  # 5 days
                'pickup_location': 'Sunny Organic Farm, 789 Rural Route 1 (farm stand)',
                'special_instructions': 'Vegetables are at peak ripeness. Use quickly or preserve by canning/freezing.'
            },
            {
                'contributor': contributors[2],
                'name': 'Organic Leafy Greens',
                'category': categories['Vegetables'],
                'description': 'Fresh spinach, kale, and lettuce. Some outer leaves may be yellowing but centers are crisp.',
                'quantity': 8,
                'unit': 'kg',
                'expiry_hours': 96,  # 4 days
                'pickup_location': 'Sunny Organic Farm, 789 Rural Route 1 (farm stand)',
                'special_instructions': 'Remove outer leaves if needed. Wash thoroughly before use. Great for salads or cooking.'
            },

            # City Center Bakery items
            {
                'contributor': contributors[3],  # City Bakery
                'name': 'Day-Old Pastry Assortment',
                'category': categories['Desserts'],
                'description': 'Mixed pastries including croissants, muffins, and Danish from yesterday. Still delicious!',
                'quantity': 30,
                'unit': 'pieces',
                'expiry_hours': 48,
                'pickup_location': 'City Center Bakery, 321 Baker Street (side entrance)',
                'special_instructions': 'Pastries are individually wrapped. Can be refreshed in oven for 2-3 minutes.'
            },
            {
                'contributor': contributors[3],
                'name': 'Artisan Bread Variety',
                'category': categories['Bakery'],
                'description': 'Whole wheat, rye, and multigrain loaves. Baked yesterday, perfect for sandwiches or toast.',
                'quantity': 20,
                'unit': 'loaves',
                'expiry_hours': 72,
                'pickup_location': 'City Center Bakery, 321 Baker Street (side entrance)',
                'special_instructions': 'Bread can be sliced on request. Freezes well for longer storage.'
            },
            {
                'contributor': contributors[3],
                'name': 'Cake and Cookie Surplus',
                'category': categories['Desserts'],
                'description': 'Assorted cakes and cookies from today\'s production. Perfect for events or sharing.',
                'quantity': 12,
                'unit': 'items',
                'expiry_hours': 96,
                'pickup_location': 'City Center Bakery, 321 Baker Street (side entrance)',
                'special_instructions': 'Cakes are in boxes, cookies in bags. Great for community events or celebrations.'
            }
        ]

        # Create food items
        food_items = []
        for item_data in food_items_data:
            expiry_date = timezone.now() + timedelta(hours=item_data['expiry_hours'])
            
            item = FoodItem.objects.create(
                contributor=item_data['contributor'],
                name=item_data['name'],
                category=item_data['category'],
                description=item_data['description'],
                quantity=item_data['quantity'],
                unit=item_data['unit'],
                expiry_date=expiry_date,
                pickup_location=item_data['pickup_location'],
                special_instructions=item_data['special_instructions'],
                status='available'
            )
            food_items.append(item)
            self.stdout.write(f'🍎 Created food item: {item.name}')

        # Create realistic donation requests
        request_messages = [
            "Hello! We serve 200+ meals daily and would love to use this food to help our community. We can pick up anytime that works for you.",
            "Our food bank distributes to 50+ families weekly. This donation would make a huge difference. Thank you for considering us!",
            "We run a community kitchen and this would help us prepare nutritious meals for those in need. We have refrigerated transport available.",
            "Our shelter houses 30 residents and we're always in need of fresh food. We can coordinate pickup at your convenience.",
            "We provide meals for seniors in our community. This food would help us serve healthy, fresh meals. We appreciate your generosity!",
            "Our organization feeds homeless individuals daily. Any food donation helps us continue this important work. Thank you!"
        ]

        # Create donation requests between recipients and available food
        for i, recipient in enumerate(recipients):
            # Each recipient requests 2-3 items
            available_items = random.sample(food_items[:8], 3)
            
            for j, item in enumerate(available_items):
                if item.status == 'available':  # Only request available items
                    requested_qty = min(item.quantity // 2, random.randint(1, 10))
                    pickup_time = timezone.now() + timedelta(hours=random.randint(6, 48))
                    
                    request = DonationRequest.objects.create(
                        food_item=item,
                        recipient=recipient,
                        requested_quantity=requested_qty,
                        message=random.choice(request_messages),
                        pickup_time=pickup_time,
                        status='pending' if j < 2 else 'approved'  # Mix of pending and approved
                    )
                    
                    # Update item status if approved
                    if request.status == 'approved':
                        item.status = 'reserved'
                        item.save()
                    
                    self.stdout.write(f'📋 Created request: {recipient.organization_name} → {item.name}')

        # Create comprehensive meal plans
        meal_plans_data = [
            {
                'user': individuals[0],  # John Smith
                'title': 'Zero-Waste Vegetable Stir Fry',
                'description': 'A colorful stir fry using leftover vegetables and reducing food waste',
                'ingredients': '''Mixed leftover vegetables (2 cups) - any combination works!
Cooked rice or noodles (2 cups)
Soy sauce (3 tbsp)
Garlic (3 cloves, minced)
Fresh ginger (1 inch, grated)
Vegetable oil (2 tbsp)
Green onions (2, chopped)
Sesame seeds (1 tbsp, optional)''',
                'instructions': '''1. Heat oil in a large wok or skillet over high heat
2. Add garlic and ginger, stir-fry for 30 seconds until fragrant
3. Add harder vegetables first (carrots, broccoli) and cook 2-3 minutes
4. Add softer vegetables (bell peppers, zucchini) and cook 2 minutes more
5. Add cooked rice or noodles and toss to combine
6. Pour soy sauce over everything and stir well
7. Cook for 1-2 minutes until heated through
8. Garnish with green onions and sesame seeds
9. Serve immediately and enjoy your waste-reducing meal!

💡 Tip: This recipe works with ANY leftover vegetables - be creative!''',
                'servings': 4,
                'prep_time': 15,
                'ai_generated': False
            },
            {
                'user': individuals[1],  # Mary Johnson
                'title': 'Banana Bread from Overripe Bananas',
                'description': 'Transform brown bananas into delicious, moist banana bread',
                'ingredients': '''Overripe bananas (4 large, very brown)
All-purpose flour (2 cups)
Sugar (3/4 cup)
Melted butter (1/3 cup)
Egg (1 large)
Vanilla extract (1 tsp)
Baking soda (1 tsp)
Salt (1/2 tsp)
Optional: chopped walnuts (1/2 cup)''',
                'instructions': '''1. Preheat oven to 350°F (175°C) and grease a 9x5 inch loaf pan
2. In a large bowl, mash the overripe bananas until smooth
3. Mix in melted butter until combined
4. Add sugar, beaten egg, and vanilla extract
5. Sprinkle baking soda and salt over the mixture and stir
6. Add flour and mix until just combined (don't overmix!)
7. Fold in nuts if using
8. Pour batter into prepared loaf pan
9. Bake for 60-65 minutes until golden brown and toothpick comes out clean
10. Cool in pan for 10 minutes, then turn out onto wire rack
11. Slice and enjoy your rescued banana creation!

🍌 Perfect way to use bananas that are too ripe to eat fresh!''',
                'servings': 10,
                'prep_time': 80,
                'ai_generated': False
            },
            {
                'user': individuals[2],  # Sarah Wilson
                'title': 'AI-Generated Leftover Magic Bowl',
                'description': 'AI-created recipe using common leftover ingredients to minimize waste',
                'ingredients': '''Leftover cooked rice (2 cups)
Any leftover vegetables (1-2 cups)
Eggs (2-3)
Cheese (1/2 cup, any type)
Leftover herbs or greens
Olive oil (2 tbsp)
Salt and pepper to taste
Hot sauce or soy sauce (optional)''',
                'instructions': '''1. Heat olive oil in a large skillet over medium heat
2. Add leftover rice and spread in an even layer
3. Let rice get crispy on the bottom (3-4 minutes)
4. Push rice to one side of the pan
5. Crack eggs into the empty space and scramble
6. Add any leftover vegetables and heat through
7. Mix everything together in the pan
8. Add cheese and let it melt
9. Season with salt, pepper, and your favorite sauce
10. Top with fresh herbs if available
11. Serve hot and feel good about reducing waste!

🤖 This AI-generated recipe adapts to whatever leftovers you have!''',
                'servings': 2,
                'prep_time': 12,
                'ai_generated': True
            },
            {
                'user': individuals[3],  # Mike Brown
                'title': 'Rescue Smoothie Bowl',
                'description': 'Turn overripe fruits into a nutritious and Instagram-worthy breakfast',
                'ingredients': '''Overripe bananas (2, frozen works great)
Any soft/overripe fruits (1 cup) - berries, mango, etc.
Yogurt or milk (1/2 cup)
Honey (1 tbsp, optional)
Granola (1/4 cup)
Nuts or seeds (2 tbsp)
Fresh fruit for topping (if available)''',
                'instructions': '''1. Add overripe bananas and other soft fruits to blender
2. Add yogurt or milk and honey
3. Blend until smooth and thick (like soft-serve ice cream)
4. Pour into a bowl
5. Top with granola, nuts, seeds, and any fresh fruit
6. Take a photo for social media! 📸
7. Enjoy your rescued fruit creation

🍓 Great way to use fruits that are too soft for eating fresh!''',
                'servings': 1,
                'prep_time': 5,
                'ai_generated': True
            },
            {
                'user': individuals[0],  # John Smith (second recipe)
                'title': 'Herb-Crusted Leftover Bread',
                'description': 'Transform day-old bread into crispy, flavorful breadcrumbs or croutons',
                'ingredients': '''Day-old bread (4-6 slices)
Olive oil (3 tbsp)
Garlic powder (1 tsp)
Dried herbs (2 tsp) - oregano, thyme, basil
Salt (1/2 tsp)
Black pepper (1/4 tsp)
Parmesan cheese (2 tbsp, optional)''',
                'instructions': '''1. Preheat oven to 375°F (190°C)
2. Cut day-old bread into cubes or tear into pieces
3. Toss bread with olive oil until evenly coated
4. Sprinkle with garlic powder, herbs, salt, and pepper
5. Add Parmesan if using
6. Spread on baking sheet in single layer
7. Bake 10-15 minutes until golden and crispy
8. Use as croutons for salads or soup
9. Or pulse in food processor for seasoned breadcrumbs
10. Store in airtight container for up to 1 week

🍞 Never throw away day-old bread again!''',
                'servings': 4,
                'prep_time': 20,
                'ai_generated': False
            }
        ]

        # Create meal plans
        for plan_data in meal_plans_data:
            plan = MealPlan.objects.create(**plan_data)
            self.stdout.write(f'🍽️ Created meal plan: {plan.title}')

        # Create sample notifications
        notification_data = [
            {
                'user': contributors[0],
                'title': 'New Donation Request',
                'message': f'{recipients[0].organization_name} has requested your Gourmet Caesar Salad Mix. Please review and respond.',
                'type': 'donation_request',
                'is_read': False
            },
            {
                'user': recipients[0],
                'title': 'Donation Request Approved',
                'message': f'Great news! {contributors[1].organization_name} has approved your request for Dairy Variety Pack.',
                'type': 'donation_request',
                'is_read': False
            },
            {
                'user': contributors[1],
                'title': 'Food Expiry Alert',
                'message': 'Your Overripe Banana Bundle expires in 2 days. Consider promoting it for quick pickup.',
                'type': 'expiry_alert',
                'is_read': True
            },
            {
                'user': individuals[0],
                'title': 'New Food Available Nearby',
                'message': 'Fresh vegetables are now available at Sunny Organic Farm, just 5 miles from you!',
                'type': 'system',
                'is_read': False
            }
        ]

        for notif_data in notification_data:
            notification = Notification.objects.create(**notif_data)
            self.stdout.write(f'🔔 Created notification: {notification.title}')

        # Summary
        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS('🎉 COMPREHENSIVE SAMPLE DATA CREATED SUCCESSFULLY!'))
        self.stdout.write('')
        self.stdout.write(self.style.WARNING('📋 LOGIN CREDENTIALS:'))
        self.stdout.write('')
        self.stdout.write('👑 ADMIN ACCOUNT:')
        self.stdout.write('   Username: admin')
        self.stdout.write('   Password: admin123')
        self.stdout.write('')
        self.stdout.write('🏪 CONTRIBUTOR ACCOUNTS (Restaurants/Groceries):')
        self.stdout.write('   Username: greenbistro    | Password: restaurant123')
        self.stdout.write('   Username: freshmarket    | Password: grocery123')
        self.stdout.write('   Username: organicfarm    | Password: farm123')
        self.stdout.write('   Username: citybakery     | Password: bakery123')
        self.stdout.write('')
        self.stdout.write('🏦 RECIPIENT ACCOUNTS (Food Banks/Shelters):')
        self.stdout.write('   Username: cityfoodbank   | Password: foodbank123')
        self.stdout.write('   Username: hopeshelter    | Password: shelter123')
        self.stdout.write('   Username: communitykitchen | Password: kitchen123')
        self.stdout.write('   Username: seniorcare     | Password: senior123')
        self.stdout.write('')
        self.stdout.write('👤 INDIVIDUAL ACCOUNTS:')
        self.stdout.write('   Username: johnsmith      | Password: individual123')
        self.stdout.write('   Username: maryjohnson    | Password: individual123')
        self.stdout.write('   Username: sarahwilson    | Password: individual123')
        self.stdout.write('   Username: mikebrown      | Password: individual123')
        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS('📊 SAMPLE DATA INCLUDES:'))
        self.stdout.write(f'   • {len(contributors)} Contributors with realistic food items')
        self.stdout.write(f'   • {len(recipients)} Recipients with active donation requests')
        self.stdout.write(f'   • {len(individuals)} Individual users with meal plans')
        self.stdout.write(f'   • {len(food_items)} Food items across all categories')
        self.stdout.write(f'   • Multiple donation requests in various states')
        self.stdout.write(f'   • {len(meal_plans_data)} Detailed meal plans (AI and manual)')
        self.stdout.write(f'   • Sample notifications and alerts')
        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS('🚀 YOUR FOODSAVER PLATFORM IS NOW FULLY POPULATED!'))
        self.stdout.write('   Visit http://127.0.0.1:8000 to explore all features')
