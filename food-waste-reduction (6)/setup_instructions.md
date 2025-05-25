# 🚀 FoodSaver Setup Instructions

## Step-by-Step Guide to Run the Project in VS Code

### Prerequisites
- Python 3.8 or higher installed
- VS Code installed
- Git installed (optional)

### Method 1: Download and Setup (Easiest)

1. **Download the Project Files**
   - Copy all the files from the code project above
   - Create a new folder on your computer called `foodsaver-project`
   - Save all files in their respective directories

2. **Open in VS Code**
   \`\`\`bash
   # Open VS Code and navigate to your project folder
   # Or use command line:
   code foodsaver-project
   \`\`\`

3. **Create Virtual Environment**
   \`\`\`bash
   # Open terminal in VS Code (Ctrl+` or View > Terminal)
   python -m venv venv
   
   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   
   # On Mac/Linux:
   source venv/bin/activate
   \`\`\`

4. **Install Dependencies**
   \`\`\`bash
   pip install Django==4.2.7
   pip install Pillow
   pip install google-generativeai
   \`\`\`

5. **Setup Database**
   \`\`\`bash
   # Create database tables
   python manage.py makemigrations
   python manage.py migrate
   \`\`\`

6. **Create Sample Data**
   \`\`\`bash
   # Create superuser for admin access
   python manage.py createsuperuser
   
   # Follow prompts to create admin account
   \`\`\`

7. **Run the Server**
   \`\`\`bash
   python manage.py runserver
   \`\`\`

8. **Access the Application**
   - Open browser and go to: http://127.0.0.1:8000
   - Admin panel: http://127.0.0.1:8000/admin

### Method 2: Quick Setup Script

Create a file called `setup.py` and run it:

\`\`\`python
import os
import subprocess
import sys

def run_command(command):
    """Run a command and print output"""
    print(f"Running: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    else:
        print(f"Success: {result.stdout}")

def setup_project():
    """Setup the Django project"""
    print("🚀 Setting up FoodSaver Project...")
    
    # Install dependencies
    run_command("pip install Django==4.2.7 Pillow google-generativeai")
    
    # Setup database
    run_command("python manage.py makemigrations FoodApp")
    run_command("python manage.py migrate")
    
    # Create sample categories
    print("Creating sample data...")
    from django.core.management import execute_from_command_line
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Mainproj.settings')
    
    print("✅ Setup complete!")
    print("Run 'python manage.py runserver' to start the application")

if __name__ == "__main__":
    setup_project()
\`\`\`

### Configuration Steps

1. **Get Gemini API Key (Optional for AI features)**
   - Go to: https://makersuite.google.com/app/apikey
   - Create a free account
   - Generate API key
   - Update `settings.py`:
   \`\`\`python
   GEMINI_API_KEY = 'your-actual-api-key-here'
   \`\`\`

2. **Create Sample Data**
   \`\`\`python
   # Run this in Django shell: python manage.py shell
   from FoodApp.models import FoodCategory, User
   
   # Create categories
   categories = [
       {'name': 'Fruits', 'icon': '🍎'},
       {'name': 'Vegetables', 'icon': '🥕'},
       {'name': 'Dairy', 'icon': '🥛'},
       {'name': 'Meat', 'icon': '🥩'},
       {'name': 'Bakery', 'icon': '🍞'},
   ]
   
   for cat in categories:
       FoodCategory.objects.get_or_create(**cat)
   
   print("Sample categories created!")
   \`\`\`

### Testing the Application

1. **Register Test Users**
   - Go to: http://127.0.0.1:8000/register/
   - Create accounts for different roles:
     - Restaurant (Contributor)
     - Charity (Recipient)
     - Individual

2. **Test Features**
   - Add food items as restaurant
   - Browse food as charity
   - Request donations
   - Try AI meal planner
   - View analytics

### Troubleshooting

**Common Issues:**

1. **Module not found error**
   \`\`\`bash
   # Make sure virtual environment is activated
   pip install -r requirements.txt
   \`\`\`

2. **Database errors**
   \`\`\`bash
   # Delete db.sqlite3 and migrations, then:
   python manage.py makemigrations FoodApp
   python manage.py migrate
   \`\`\`

3. **Static files not loading**
   \`\`\`bash
   python manage.py collectstatic
   \`\`\`

4. **AI features not working**
   - Install: `pip install google-generativeai`
   - Add API key to settings.py
   - Or use without AI (basic meal plans will be created)

### Project Structure
\`\`\`
foodsaver-project/
├── manage.py
├── requirements.txt
├── Mainproj/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── FoodApp/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── templates/
│   ├── base.html
│   ├── FoodApp/
│   │   └── home.html
│   └── registration/
│       ├── login.html
│       └── register.html
├── static/
├── media/
└── db.sqlite3
\`\`\`

### Next Steps

1. **Customize the platform**
   - Add your organization details
   - Modify colors and branding
   - Add more food categories

2. **Deploy to production**
   - Use PostgreSQL database
   - Configure static file serving
   - Set up domain and SSL

3. **Add more features**
   - Email notifications
   - Google Maps integration
   - Mobile app
   - Payment processing

### Support

If you encounter any issues:
1. Check the terminal for error messages
2. Ensure all dependencies are installed
3. Verify Python version (3.8+)
4. Make sure virtual environment is activated

**Happy coding! 🎉**
\`\`\`

## 📋 Complete Setup Checklist

Here's your step-by-step guide to get the FoodSaver platform running on your laptop:

### ✅ **Quick Start (5 minutes)**

1. **Create project folder**
   \`\`\`bash
   mkdir foodsaver-project
   cd foodsaver-project
   \`\`\`

2. **Copy all the code files** from above into the correct folder structure

3. **Open in VS Code**
   \`\`\`bash
   code .
   \`\`\`

4. **Open terminal in VS Code** (Ctrl + ` or View → Terminal)

5. **Install Django**
   \`\`\`bash
   pip install Django==4.2.7 Pillow
   \`\`\`

6. **Setup database**
   \`\`\`bash
   python manage.py makemigrations FoodApp
   python manage.py migrate
   \`\`\`

7. **Create admin user**
   \`\`\`bash
   python manage.py createsuperuser
   \`\`\`

8. **Run the server**
   \`\`\`bash
   python manage.py runserver
   \`\`\`

9. **Open browser** → http://127.0.0.1:8000

### 🎯 **Easy Download Method**

The easiest way to get all files:
1. Copy each code block above
2. Create the file with the exact name shown
3. Paste the content
4. Save in the correct folder structure

### 🔧 **Optional: AI Features**

To enable AI meal planning:
\`\`\`bash
pip install google-generativeai
\`\`\`

Get free API key from: https://makersuite.google.com/app/apikey

Update in `settings.py`:
\`\`\`python
GEMINI_API_KEY = 'your-actual-api-key-here'
\`\`\`

### 🚀 **You're Ready!**

Your platform will have:
- ✅ User registration with roles
- ✅ Food item management
- ✅ Donation system
- ✅ AI meal planning (if API key added)
- ✅ Analytics dashboard
- ✅ Responsive design
- ✅ Admin panel

**Default login after setup:**
- Create your own admin account during setup
- Register test users through the web interface

The platform is now ready for your hackathon demo! 🏆
