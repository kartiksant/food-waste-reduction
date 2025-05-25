# 🚀 Deployment Guide for FoodSaver Platform

## Local Development Setup

### Step 1: Download and Setup
1. **Create project folder**
   \`\`\`bash
   mkdir foodsaver-project
   cd foodsaver-project
   \`\`\`

2. **Copy all files** from the code project above

3. **Create virtual environment**
   \`\`\`bash
   python -m venv venv
   
   # Activate (Windows)
   venv\Scripts\activate
   
   # Activate (Mac/Linux)
   source venv/bin/activate
   \`\`\`

4. **Install dependencies**
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

5. **Setup database**
   \`\`\`bash
   python manage.py makemigrations FoodApp
   python manage.py migrate
   python manage.py createsuperuser
   \`\`\`

6. **Run locally**
   \`\`\`bash
   python manage.py runserver
   \`\`\`

## Production Deployment Options

### Option 1: Vercel (Recommended)
1. **Install Vercel CLI**
   \`\`\`bash
   npm install -g vercel
   \`\`\`

2. **Deploy**
   \`\`\`bash
   vercel --prod
   \`\`\`

### Option 2: Railway
1. **Connect GitHub repo**
2. **Add environment variables:**
   - `DJANGO_SETTINGS_MODULE=Mainproj.settings`
   - `SECRET_KEY=your-secret-key`
   - `DEBUG=False`

### Option 3: Render
1. **Create new Web Service**
2. **Build Command:** `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
3. **Start Command:** `gunicorn Mainproj.wsgi:application`

### Option 4: Heroku
1. **Install Heroku CLI**
2. **Create app**
   \`\`\`bash
   heroku create foodsaver-app
   git push heroku main
   \`\`\`

## Environment Variables

Set these in your deployment platform:

\`\`\`
SECRET_KEY=your-super-secret-key-here
DEBUG=False
GEMINI_API_KEY=your-gemini-api-key
DATABASE_URL=your-database-url (if using PostgreSQL)
\`\`\`

## Quick Local Test

\`\`\`bash
# 1. Clone/download project
# 2. Install dependencies
pip install Django==4.2.7 Pillow

# 3. Setup database
python manage.py makemigrations FoodApp
python manage.py migrate

# 4. Create admin user
python manage.py createsuperuser

# 5. Run server
python manage.py runserver

# 6. Open browser: http://127.0.0.1:8000
\`\`\`

## Troubleshooting

**Common Issues:**

1. **Bun install error** - Fixed! Added package.json
2. **Module not found** - Run: `pip install -r requirements.txt`
3. **Database errors** - Run migrations: `python manage.py migrate`
4. **Static files** - Run: `python manage.py collectstatic`

## Features Working

✅ User registration with roles
✅ Food item management  
✅ Donation requests
✅ AI meal planning (with API key)
✅ Analytics dashboard
✅ Admin panel
✅ Responsive design
✅ Production-ready deployment

## Default Credentials

After setup:
- **Admin:** Use the superuser you created
- **Test Users:** Register through the web interface

Your platform is now ready for deployment! 🎉
\`\`\`
