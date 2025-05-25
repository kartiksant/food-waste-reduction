# 🧪 FoodSaver Platform Testing Guide

## 🚀 Quick Setup & Population

### Option 1: Run the Script (Recommended)
\`\`\`bash
# Linux/Mac
chmod +x populate_data.sh
./populate_data.sh

# Windows
populate_data.bat
\`\`\`

### Option 2: Manual Commands
\`\`\`bash
python manage.py makemigrations FoodApp
python manage.py migrate
python manage.py create_sample_data
python manage.py runserver
\`\`\`

## 🔑 Test Accounts

### 👑 Admin Account
- **Username:** `admin`
- **Password:** `admin123`
- **Features:** Full platform management, analytics, user oversight

### 🏪 Contributor Accounts (Food Providers)
| Username | Password | Organization | Type |
|----------|----------|--------------|------|
| `greenbistro` | `restaurant123` | Green Bistro Restaurant | Restaurant |
| `freshmarket` | `grocery123` | Fresh Market Grocery | Grocery Store |
| `organicfarm` | `farm123` | Sunny Organic Farm | Farm |
| `citybakery` | `bakery123` | City Center Bakery | Bakery |

### 🏦 Recipient Accounts (Food Recipients)
| Username | Password | Organization | Type |
|----------|----------|--------------|------|
| `cityfoodbank` | `foodbank123` | City Food Bank | Food Bank |
| `hopeshelter` | `shelter123` | Hope Community Shelter | Shelter |
| `communitykitchen` | `kitchen123` | Community Kitchen Network | Community Kitchen |
| `seniorcare` | `senior123` | Senior Care Nutrition Program | Senior Care |

### 👤 Individual Accounts
| Username | Password | Name | Role |
|----------|----------|------|------|
| `johnsmith` | `individual123` | John Smith | Individual |
| `maryjohnson` | `individual123` | Mary Johnson | Individual |
| `sarahwilson` | `individual123` | Sarah Wilson | Individual |
| `mikebrown` | `individual123` | Mike Brown | Individual |

## 🧪 Testing Scenarios

### 1. **Admin Dashboard Testing**
\`\`\`
Login: admin/admin123
✅ View platform statistics
✅ Access Django admin panel
✅ Monitor all user activity
✅ Check global analytics
\`\`\`

### 2. **Contributor Workflow Testing**
\`\`\`
Login: greenbistro/restaurant123
✅ Add new food items
✅ View expiring items alerts
✅ Manage incoming donation requests
✅ Approve/reject requests
✅ Track donation impact
\`\`\`

### 3. **Recipient Workflow Testing**
\`\`\`
Login: cityfoodbank/foodbank123
✅ Browse available food items
✅ Request food donations
✅ Track request status
✅ View pickup instructions
✅ Check organization impact
\`\`\`

### 4. **Individual User Testing**
\`\`\`
Login: johnsmith/individual123
✅ Use AI meal planner
✅ Create custom meal plans
✅ Browse nearby food
✅ Request small donations
✅ Track personal impact
\`\`\`

## 📊 Sample Data Included

### 🍎 Food Items (15+ realistic items)
- **Green Bistro:** Gourmet salads, artisan bread, roasted vegetables
- **Fresh Market:** Overripe bananas, dairy products, cosmetic-defect produce
- **Organic Farm:** Fresh carrots, seasonal vegetables, leafy greens
- **City Bakery:** Day-old pastries, artisan breads, surplus desserts

### 📋 Donation Requests
- Multiple pending requests between organizations
- Approved requests showing workflow
- Realistic pickup times and messages
- Various quantities and urgency levels

### 🍽️ Meal Plans
- **Zero-Waste Stir Fry** (using leftover vegetables)
- **Banana Bread** (from overripe bananas)
- **AI-Generated Magic Bowl** (adaptive leftovers recipe)
- **Rescue Smoothie Bowl** (overripe fruit transformation)
- **Herb-Crusted Bread** (day-old bread rescue)

### 🔔 Notifications
- New donation requests
- Approval confirmations
- Expiry alerts
- System notifications

## 🎯 Key Features to Test

### ✅ **Food Management**
1. Add food items with photos
2. Set expiry dates and urgency
3. Update pickup locations
4. Track item status changes

### ✅ **Donation System**
1. Browse available food by category
2. Filter by urgency and location
3. Submit donation requests
4. Approve/reject requests
5. Track pickup coordination

### ✅ **AI Meal Planning**
1. Enter available ingredients
2. Set dietary preferences
3. Generate AI recipes (if API key configured)
4. Save and view meal plans
5. Share recipes

### ✅ **Analytics Dashboard**
1. Personal impact metrics
2. Environmental calculations
3. Global platform statistics
4. Achievement tracking
5. Progress visualization

### ✅ **User Management**
1. Role-based access control
2. Organization profiles
3. Verification status
4. Contact information

## 🔍 Testing Checklist

### **Navigation & UI**
- [ ] All menu items work
- [ ] Responsive design on mobile
- [ ] Forms submit correctly
- [ ] Error messages display
- [ ] Success notifications appear

### **Authentication**
- [ ] Login/logout functionality
- [ ] Registration process
- [ ] Password changes
- [ ] Role-based redirects

### **Core Features**
- [ ] Food item CRUD operations
- [ ] Donation request workflow
- [ ] Meal plan creation
- [ ] Analytics calculations
- [ ] Notification system

### **Data Integrity**
- [ ] Expiry date calculations
- [ ] Urgency level updates
- [ ] Status transitions
- [ ] Quantity tracking

## 🐛 Common Issues & Solutions

### **Database Issues**
\`\`\`bash
# Reset database if needed
rm db.sqlite3
python manage.py makemigrations FoodApp
python manage.py migrate
python manage.py create_sample_data
\`\`\`

### **Static Files Not Loading**
\`\`\`bash
python manage.py collectstatic --clear
python manage.py collectstatic
\`\`\`

### **AI Features Not Working**
1. Install: `pip install google-generativeai`
2. Get API key from: https://makersuite.google.com/app/apikey
3. Update `settings.py`: `GEMINI_API_KEY = 'your-key'`

## 📈 Success Metrics

Your platform is working correctly when:
- ✅ All 15 user accounts can login
- ✅ 15+ food items are visible
- ✅ Donation requests can be created and managed
- ✅ Meal plans generate and save
- ✅ Analytics show realistic data
- ✅ Notifications appear for relevant actions
- ✅ All dashboards load without errors

## 🎉 Demo Flow

**Perfect demo sequence:**
1. **Admin view** → Show platform overview
2. **Restaurant login** → Add food item, show expiry tracking
3. **Food bank login** → Browse food, make request
4. **Restaurant approval** → Approve the request
5. **Individual user** → Use AI meal planner
6. **Analytics** → Show environmental impact

**Your FoodSaver platform is now ready for comprehensive testing!** 🚀
