#!/bin/bash

echo "🌱 FoodSaver - Populating Extensive Food Data"
echo "============================================="

echo "📦 Installing dependencies..."
pip install -r requirements.txt

echo "🗄️ Setting up database..."
python manage.py makemigrations FoodApp
python manage.py migrate

echo "🌱 Creating extensive food data..."
python manage.py populate_extensive_data

echo "🧹 Collecting static files..."
python manage.py collectstatic --noinput

echo ""
echo "✅ EXTENSIVE DATA POPULATION COMPLETE!"
echo ""
echo "🎯 Your platform now has:"
echo "   • 15+ realistic food items across all categories"
echo "   • Active donation requests in various states"
echo "   • Sample meal plans and notifications"
echo "   • Complete user accounts for testing"
echo ""
echo "🚀 Starting development server..."
echo "📱 Open: http://127.0.0.1:8000"
echo ""
echo "🔑 Test Accounts:"
echo "   Admin: admin/admin123"
echo "   Restaurant: greenbistro/restaurant123"
echo "   Grocery: freshmarket/grocery123"
echo "   Food Bank: cityfoodbank/foodbank123"
echo "   Individual: johnsmith/individual123"
echo ""

python manage.py runserver
