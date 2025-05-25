@echo off
echo 🚀 Setting up Complete Food Waste Reduction Platform...

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo 📦 Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo 📚 Installing dependencies...
pip install -r requirements.txt

REM Create necessary directories
echo 📁 Creating directories...
if not exist "media\food_images" mkdir media\food_images
if not exist "static" mkdir static
if not exist "staticfiles" mkdir staticfiles

REM Database setup
echo 🗄️ Setting up database...
python manage.py makemigrations
python manage.py migrate

REM Create superuser
echo 👤 Creating superuser...
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@foodsaver.com', 'admin123', role='admin')"

REM Fix and create categories
echo 🏷️ Setting up food categories...
python manage.py fix_categories

REM Create sample data
echo 📊 Creating sample data...
python manage.py create_sample_data

REM Create extensive test data
echo 🎯 Creating extensive test data...
python manage.py populate_extensive_data

REM Collect static files
echo 🎨 Collecting static files...
python manage.py collectstatic --noinput

echo ✅ Setup complete!
echo.
echo 🎉 Your Food Waste Reduction Platform is ready!
echo.
echo 📋 Test Accounts:
echo    Admin: admin / admin123
echo    Restaurant: greenbistro / restaurant123
echo    Food Bank: cityfoodbank / foodbank123
echo    Individual: johnsmith / individual123
echo.
echo 🚀 Start the server:
echo    python manage.py runserver
echo.
echo 🌐 Access the platform:
echo    http://127.0.0.1:8000
echo.
echo 🤖 AI Features Available:
echo    - Waste Prediction Analysis
echo    - Smart Recipient Notifications
echo    - Demand Pattern Analysis
echo    - Personalized Recommendations

pause
