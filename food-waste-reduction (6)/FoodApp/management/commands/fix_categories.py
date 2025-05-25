from django.core.management.base import BaseCommand
from FoodApp.models import FoodCategory

class Command(BaseCommand):
    help = 'Create and fix food categories'
    
    def handle(self, *args, **options):
        categories = [
            'Vegetables & Fruits',
            'Grains & Cereals', 
            'Dairy Products',
            'Meat & Poultry',
            'Seafood',
            'Bakery Items',
            'Beverages',
            'Prepared Meals',
            'Snacks & Confectionery',
            'Frozen Foods',
            'Canned & Packaged',
            'Others'
        ]
        
        created_count = 0
        for category_name in categories:
            category, created = FoodCategory.objects.get_or_create(
                name=category_name,
                defaults={'description': f'{category_name} category for food items'}
            )
            if created:
                created_count += 1
                self.stdout.write(f'Created category: {category_name}')
            else:
                self.stdout.write(f'Category already exists: {category_name}')
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully processed {len(categories)} categories. Created {created_count} new categories.')
        )
