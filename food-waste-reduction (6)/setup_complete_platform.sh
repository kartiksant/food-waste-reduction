#!/bin/bash

echo "🚀 Setting up Complete Food Waste Reduction Platform..."

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📚 Installing dependencies..."
pip install -r requirements.txt

# Create necessary directories
echo "📁 Creating directories..."
mkdir -p media/food_images
mkdir -p static
mkdir -p staticfiles

# Database setup
echo "🗄️ Setting up database..."
python manage.py makemigrations
python manage.py migrate

# Create superuser if it doesn't exist
echo "👤 Creating superuser..."
python manage.py shell << EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@foodsaver.com', 'admin123', role='admin')
    print('Superuser created: admin/admin123')
else:
    print('Superuser already exists')
EOF

# Fix and create categories
echo "🏷️ Setting up food categories..."
python manage.py fix_categories

# Create sample data
echo "📊 Creating sample data..."
python manage.py create_sample_data

# Create extensive test data
echo "🎯 Creating extensive test data..."
python manage.py populate_extensive_data

# Collect static files
echo "🎨 Collecting static files..."
python manage.py collectstatic --noinput

echo "✅ Setup complete!"
echo ""
echo "🎉 Your Food Waste Reduction Platform is ready!"
echo ""
echo "📋 Test Accounts:"
echo "   Admin: admin / admin123"
echo "   Restaurant: greenbistro / restaurant123"
echo "   Food Bank: cityfoodbank / foodbank123"
echo "   Individual: johnsmith / individual123"
echo ""
echo "🚀 Start the server:"
echo "   python manage.py runserver"
echo ""
echo "🌐 Access the platform:"
echo "   http://127.0.0.1:8000"
echo ""
echo "🤖 AI Features Available:"
echo "   - Waste Prediction Analysis"
echo "   - Smart Recipient Notifications"
echo "   - Demand Pattern Analysis"
echo "   - Personalized Recommendations"
