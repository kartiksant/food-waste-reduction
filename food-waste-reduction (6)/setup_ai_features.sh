#!/bin/bash

echo "🤖 FoodSaver - Setting up AI Features"
echo "===================================="

echo "📦 Installing AI dependencies..."
pip install google-generativeai

echo "🗄️ Creating database migrations..."
python manage.py makemigrations FoodApp

echo "🗄️ Applying migrations..."
python manage.py migrate

echo "🌱 Populating with extensive data..."
python manage.py populate_extensive_data

echo "🧹 Collecting static files..."
python manage.py collectstatic --noinput

echo ""
echo "✅ AI FEATURES SETUP COMPLETE!"
echo ""
echo "🤖 AI Features Now Available:"
echo "   • Smart waste prediction using Gemini AI"
echo "   • Personalized notifications for recipients"
echo "   • Pattern recognition (e.g., 'Biryani wasted on Saturdays')"
echo "   • AI-powered meal planning with waste reduction focus"
echo "   • Demand prediction and optimization"
echo ""
echo "🔑 Your Gemini API Key is configured: AIzaSyDRyXwFFpCqWqTYIPfDyENM_Hl_h62wV_o"
echo ""
echo "🚀 Starting server..."
echo "📱 Open: http://127.0.0.1:8000"
echo ""

python manage.py runserver
