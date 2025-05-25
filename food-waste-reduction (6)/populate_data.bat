@echo off
echo 🌱 FoodSaver Platform - Comprehensive Data Population
echo ==================================================

echo 📦 Installing/updating dependencies...
pip install -r requirements.txt

echo 🗄️ Setting up database...
python manage.py makemigrations FoodApp
python manage.py migrate

echo 🌱 Creating comprehensive sample data...
python manage.py create_sample_data

echo 🧹 Collecting static files...
python manage.py collectstatic --noinput

echo.
echo ✅ SETUP COMPLETE!
echo.
echo 🚀 Starting development server...
echo 📱 Open your browser to: http://127.0.0.1:8000
echo.
echo 🔑 Quick Login Guide:
echo    Admin: admin/admin123
echo    Restaurant: greenbistro/restaurant123
echo    Food Bank: cityfoodbank/foodbank123
echo    Individual: johnsmith/individual123
echo.

REM Start the server
python manage.py runserver
