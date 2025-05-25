# 🌍 FoodSaver - Sustainable Food Waste Reduction Platform

A complete Django-based web application that connects restaurants, charities, and individuals to reduce food waste through AI-powered meal planning and smart donation coordination.

## 🚀 Quick Start Guide

### Step 1: Setup
\`\`\`bash
# Create project folder
mkdir foodsaver-project
cd foodsaver-project

# Copy all files from the code project above

# Run setup script
chmod +x setup.sh
./setup.sh
\`\`\`

### Step 2: Create Admin User
\`\`\`bash
python manage.py createsuperuser
\`\`\`

### Step 3: Run Server
\`\`\`bash
python manage.py runserver
\`\`\`

### Step 4: Open Browser
- **Main site**: http://127.0.0.1:8000
- **Admin panel**: http://127.0.0.1:8000/admin

## ✨ Features

- ✅ **Role-based Access**: Admin, Contributors, Recipients, Individuals
- ✅ **Food Management**: Add, browse, and track food items
- ✅ **Donation System**: Request and manage food donations
- ✅ **AI Meal Planning**: Generate recipes from available ingredients
- ✅ **Analytics Dashboard**: Track environmental impact
- ✅ **Responsive Design**: Works on all devices
- ✅ **Admin Panel**: Complete backend management

## 🎯 User Roles

1. **Contributors** (Restaurants/Grocers): Add surplus food items
2. **Recipients** (Charities/Food Banks): Request food donations
3. **Individuals**: Use AI meal planner and browse food
4. **Admins**: Manage the entire platform

## 🔧 Manual Setup (Alternative)

\`\`\`bash
# 1. Create virtual environment
python -m venv venv

# 2. Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install Django==4.2.7 Pillow

# 4. Setup database
python manage.py makemigrations FoodApp
python manage.py migrate

# 5. Create admin user
python manage.py createsuperuser

# 6. Run server
python manage.py runserver
\`\`\`

## 🤖 Enable AI Features (Optional)

1. Get free API key from: https://makersuite.google.com/app/apikey
2. Install AI package: `pip install google-generativeai`
3. Update `settings.py`: `GEMINI_API_KEY = 'your-actual-api-key'`

## 📁 Project Structure

\`\`\`
foodsaver-project/
├── manage.py
├── requirements.txt
├── setup.sh
├── Mainproj/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── FoodApp/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── admin.py
├── templates/
│   ├── base.html
│   ├── FoodApp/
│   └── registration/
└── static/
\`\`\`

## 🎉 Success Indicators

You'll know it's working when:
- ✅ Server starts without errors
- ✅ Home page loads with green design
- ✅ You can register new users
- ✅ Admin panel is accessible
- ✅ Navigation menu works

## 🔍 Testing the Platform

1. **Register users** with different roles
2. **Add food items** as a restaurant
3. **Request donations** as a charity
4. **Try AI meal planner** as an individual
5. **Check analytics** dashboard
6. **Explore admin panel**

## 🚨 Troubleshooting

**Common Issues:**

1. **Module not found**: `pip install -r requirements.txt`
2. **Database errors**: Delete `db.sqlite3` and run migrations again
3. **Port in use**: Use `python manage.py runserver 8001`
4. **Static files**: Run `python manage.py collectstatic`

## 🌟 Key Features Showcase

- **Smart Expiry Tracking**: Automatic urgency calculation
- **Role-based Dashboards**: Customized for each user type
- **Real-time Notifications**: Donation requests and alerts
- **Impact Analytics**: CO₂ reduction and waste metrics
- **Responsive Design**: Mobile-friendly interface
- **Admin Management**: Complete backend control

## 📞 Support

Your FoodSaver platform is now ready for:
- ✅ Local development
- ✅ Hackathon demos
- ✅ Production deployment
- ✅ Feature extensions

**Happy coding! 🎉**
