#!/bin/bash

echo "🍃 Starting FoodSaver Platform Locally..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    # Windows
    source venv/Scripts/activate
else
    # Mac/Linux
    source venv/bin/activate
fi

# Install dependencies
echo "📚 Installing dependencies..."
pip install -r requirements.txt

# Setup database
echo "🗄️ Setting up database..."
python manage.py makemigrations FoodApp
python manage.py migrate

# Create sample data
echo "🌱 Creating sample data..."
python manage.py shell << EOF
from FoodApp.models import FoodCategory, User
from django.contrib.auth import get_user_model

# Create food categories
categories = [
    {'name': 'Fruits', 'icon': '🍎', 'description': 'Fresh fruits and berries'},
    {'name': 'Vegetables', 'icon': '🥕', 'description': 'Fresh vegetables and greens'},
    {'name': 'Dairy', 'icon': '🥛', 'description': 'Milk, cheese, yogurt products'},
    {'name': 'Meat', 'icon': '🥩', 'description': 'Fresh and frozen meat products'},
    {'name': 'Bakery', 'icon': '🍞', 'description': 'Bread, pastries, baked goods'},
    {'name': 'Prepared Foods', 'icon': '🍽️', 'description': 'Ready-to-eat meals'},
]

for cat_data in categories:
    category, created = FoodCategory.objects.get_or_create(
        name=cat_data['name'],
        defaults=cat_data
    )
    if created:
        print(f'Created category: {category.name}')

print("Sample data created!")
EOF

echo "✅ Setup complete!"
echo ""
echo "🚀 Starting development server..."
echo "📱 Open your browser to: http://127.0.0.1:8000"
echo ""
echo "👤 To create an admin user, run: python manage.py createsuperuser"
echo ""

# Start the server
python manage.py runserver
