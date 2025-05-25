# ✅ FoodSaver Quick Test Checklist

## 🚀 Before You Start
\`\`\`bash
python manage.py create_sample_data
python manage.py runserver
# Open: http://127.0.0.1:8000
\`\`\`

## 🧪 5-Minute Quick Test

### 1. **Admin Test** (1 minute)
- [ ] Login: `admin/admin123`
- [ ] Dashboard loads with statistics
- [ ] Can access Django admin panel

### 2. **Restaurant Test** (2 minutes)
- [ ] Login: `greenbistro/restaurant123`
- [ ] Add new food item successfully
- [ ] View "My Items" list
- [ ] See pending donation requests
- [ ] Approve a request

### 3. **Food Bank Test** (1 minute)
- [ ] Login: `cityfoodbank/foodbank123`
- [ ] Browse available food items
- [ ] Submit donation request
- [ ] View "My Requests" status

### 4. **Individual Test** (1 minute)
- [ ] Login: `johnsmith/individual123`
- [ ] Use AI Meal Planner
- [ ] Generate recipe successfully
- [ ] View meal plan details

## 🎯 Key Success Indicators

- ✅ All logins work
- ✅ Dashboards show real data
- ✅ Food items display correctly
- ✅ Donation workflow functions
- ✅ AI meal planner generates recipes
- ✅ Analytics page loads without errors
- ✅ Navigation works between all sections

## 🔧 If Something Breaks

\`\`\`bash
# Reset everything
rm db.sqlite3
python manage.py makemigrations FoodApp
python manage.py migrate
python manage.py create_sample_data
python manage.py runserver
\`\`\`

**Your platform should now work perfectly!** 🎉
