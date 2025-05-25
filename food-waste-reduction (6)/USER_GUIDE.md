# 🍃 FoodSaver Platform - Complete User Guide

## 🚀 Getting Started

### Step 1: Setup and Run the Platform
\`\`\`bash
# 1. Populate with test data
python manage.py create_sample_data

# 2. Start the server
python manage.py runserver

# 3. Open browser to: http://127.0.0.1:8000
\`\`\`

### Step 2: Access the Platform
- **Homepage:** http://127.0.0.1:8000
- **Admin Panel:** http://127.0.0.1:8000/admin

---

## 👑 ADMIN USER TESTING

### Login as Admin
\`\`\`
Username: admin
Password: admin123
\`\`\`

### What You Can Do:
1. **View Platform Overview**
   - Total users across all roles
   - Food items in the system
   - Pending donation requests
   - Daily food saved metrics

2. **Access Django Admin Panel**
   - Click "Django Admin" button
   - Manage all users, food items, categories
   - View detailed database records

3. **Monitor Platform Activity**
   - Recent donations
   - Platform statistics
   - User activity overview

---

## 🏪 CONTRIBUTOR (RESTAURANT/GROCERY) TESTING

### Login as Restaurant Owner
\`\`\`
Username: greenbistro
Password: restaurant123
Organization: Green Bistro Restaurant
\`\`\`

### Step-by-Step Contributor Workflow:

#### 1. **Add New Food Item**
1. Click **"Add Food Item"** from dashboard or navigation
2. Fill out the form:
   - **Food Name:** "Fresh Garden Salad Mix"
   - **Category:** Select "Vegetables"
   - **Description:** "Mixed greens with cherry tomatoes, made fresh today but approaching end of service"
   - **Quantity:** 10
   - **Unit:** "portions"
   - **Expiry Date:** Tomorrow at 6 PM
   - **Pickup Location:** "Green Bistro Restaurant, 123 Main Street (back entrance)"
   - **Special Instructions:** "Salads are in individual containers. Best consumed within 12 hours."
3. Click **"Add Food Item"**
4. ✅ **Success:** Item appears in your food list

#### 2. **View Your Food Items**
1. Click **"My Items"** from navigation
2. See all your contributed items with:
   - Status badges (Available, Reserved, Donated)
   - Urgency levels (Critical, High, Medium, Low)
   - Expiry dates
   - Quantities

#### 3. **Manage Donation Requests**
1. Click **"Manage Requests"** from dashboard
2. You'll see requests from food banks/shelters
3. For each request, you can:
   - **View requester details**
   - **Read their message**
   - **See requested quantity**
   - **Approve** or **Reject** the request

#### 4. **Approve a Donation Request**
1. Find a pending request
2. Click **"Approve"** button
3. ✅ **Result:** 
   - Request status changes to "Approved"
   - Food item status changes to "Reserved"
   - Recipient gets notification

#### 5. **View Your Impact**
1. Click **"Analytics"** from navigation
2. See your contribution metrics:
   - Total food saved (kg)
   - Number of donations made
   - CO₂ emissions reduced
   - Money saved by recipients

---

## 🏦 RECIPIENT (FOOD BANK/SHELTER) TESTING

### Login as Food Bank
\`\`\`
Username: cityfoodbank
Password: foodbank123
Organization: City Food Bank
\`\`\`

### Step-by-Step Recipient Workflow:

#### 1. **Browse Available Food**
1. Click **"Browse Food"** from navigation
2. See all available food items with:
   - Photos (if uploaded)
   - Descriptions and quantities
   - Expiry dates and urgency
   - Contributor information
   - Pickup locations

#### 2. **Filter Food Items**
1. Use the filter section:
   - **Category:** Select "Vegetables" or "Bakery"
   - **Urgency:** Select "High" to see items expiring soon
2. Click **"Filter"** to apply
3. Click **"Clear"** to reset filters

#### 3. **Request a Food Donation**
1. Find an item you want (e.g., "Overripe Banana Bundle")
2. Click **"Request Donation"** button
3. Fill out the request form:
   - **Requested Quantity:** 25 (out of 50 available)
   - **Preferred Pickup Time:** Tomorrow at 2 PM
   - **Message:** "Hello! City Food Bank serves 200+ families weekly. These bananas would be perfect for our community kitchen to make banana bread for our clients. We can pick up anytime that works for you. Thank you for your generosity!"
4. Click **"Send Request"**
5. ✅ **Success:** Request is submitted to the contributor

#### 4. **Track Your Requests**
1. Click **"My Requests"** from navigation
2. See all your donation requests with:
   - **Status:** Pending, Approved, Completed, Cancelled
   - **Food item details**
   - **Requested quantities**
   - **Pickup times**
   - **Messages sent**

#### 5. **View Your Impact**
1. Click **"Analytics"** from navigation
2. See your organization's impact:
   - Food received (kg)
   - Successful donations
   - Environmental impact
   - Community benefit metrics

---

## 👤 INDIVIDUAL USER TESTING

### Login as Individual
\`\`\`
Username: johnsmith
Password: individual123
Name: John Smith
\`\`\`

### Step-by-Step Individual Workflow:

#### 1. **Use AI Meal Planner**
1. Click **"AI Meal Planner"** from navigation
2. Fill out the form:
   - **Available Ingredients:** "chicken breast, rice, broccoli, onions, garlic, soy sauce"
   - **Dietary Preferences:** "low-carb" (optional)
   - **Number of Servings:** 4
3. Click **"Generate Meal Plan with AI"**
4. ✅ **Result:** AI creates a detailed recipe with:
   - Creative meal title
   - Step-by-step instructions
   - Cooking tips
   - Waste reduction focus

#### 2. **Create Manual Meal Plan**
1. Go to **"Meal Plans"** from navigation
2. Click **"Create New Plan"** (if available) or use AI planner
3. Save the generated plan
4. View your saved meal plans

#### 3. **View Meal Plan Details**
1. Click on any meal plan from your list
2. See complete recipe with:
   - Ingredients list
   - Detailed cooking instructions
   - Prep time and servings
   - AI-generated badge (if applicable)

#### 4. **Browse Nearby Food**
1. Click **"Browse Food"** from navigation
2. See available food items in your area
3. Request small quantities for personal use

#### 5. **Track Personal Impact**
1. Click **"Analytics"** from navigation
2. View your contribution to:
   - Food waste reduction
   - Environmental impact
   - Community benefit

---

## 🧪 COMPLETE TESTING SCENARIOS

### Scenario 1: Full Donation Workflow
1. **Login as Restaurant** (greenbistro/restaurant123)
2. **Add food item** with short expiry
3. **Login as Food Bank** (cityfoodbank/foodbank123)
4. **Request the food item**
5. **Switch back to Restaurant**
6. **Approve the request**
7. **Check notifications** for both users

### Scenario 2: AI Meal Planning
1. **Login as Individual** (johnsmith/individual123)
2. **Use AI Meal Planner** with various ingredients
3. **Save multiple meal plans**
4. **View detailed recipes**
5. **Check meal plan history**

### Scenario 3: Platform Analytics
1. **Login as Admin** (admin/admin123)
2. **View platform-wide statistics**
3. **Switch to different user roles**
4. **Compare analytics across roles**
5. **Check environmental impact calculations**

### Scenario 4: Multi-User Interaction
1. **Create food items** from multiple contributors
2. **Submit requests** from multiple recipients
3. **Approve/reject** various requests
4. **Track status changes** across the platform

---

## 🔍 FEATURES TO TEST

### ✅ **Navigation & UI**
- [ ] All menu items work correctly
- [ ] Responsive design on mobile/tablet
- [ ] Forms submit without errors
- [ ] Success/error messages display
- [ ] Page loading times are reasonable

### ✅ **User Authentication**
- [ ] Login/logout functionality
- [ ] Role-based dashboard redirects
- [ ] Password change process
- [ ] Registration for new users

### ✅ **Food Management**
- [ ] Add food items with all details
- [ ] Upload food photos
- [ ] Set expiry dates and locations
- [ ] View food item lists
- [ ] Filter and search functionality

### ✅ **Donation System**
- [ ] Browse available food
- [ ] Submit donation requests
- [ ] Approve/reject requests
- [ ] Track request status
- [ ] Coordinate pickup details

### ✅ **AI Meal Planning**
- [ ] Generate recipes from ingredients
- [ ] Save meal plans
- [ ] View detailed cooking instructions
- [ ] Track meal plan history

### ✅ **Analytics Dashboard**
- [ ] Personal impact metrics
- [ ] Environmental calculations
- [ ] Platform-wide statistics
- [ ] Role-specific analytics

### ✅ **Notifications**
- [ ] Donation request alerts
- [ ] Approval confirmations
- [ ] Expiry warnings
- [ ] System notifications

---

## 🎯 SUCCESS INDICATORS

Your platform is working correctly when:

1. **All user roles can login** and see appropriate dashboards
2. **Food items can be added** with photos and details
3. **Donation requests flow** from recipients to contributors
4. **Approvals work** and update item status
5. **AI meal planner generates** realistic recipes
6. **Analytics show** meaningful data
7. **Notifications appear** for relevant actions
8. **All navigation links** work without errors

---

## 🐛 Troubleshooting

### Common Issues:

1. **Analytics page error:**
   \`\`\`bash
   # The view has been fixed in the code above
   python manage.py runserver
   \`\`\`

2. **No sample data:**
   \`\`\`bash
   python manage.py create_sample_data
   \`\`\`

3. **Static files not loading:**
   \`\`\`bash
   python manage.py collectstatic
   \`\`\`

4. **Database errors:**
   \`\`\`bash
   rm db.sqlite3
   python manage.py makemigrations FoodApp
   python manage.py migrate
   python manage.py create_sample_data
   \`\`\`

---

## 🎉 Demo Flow for Presentation

**Perfect 5-minute demo sequence:**

1. **Admin Dashboard** (30 seconds)
   - Show platform overview and statistics

2. **Restaurant Workflow** (90 seconds)
   - Login as greenbistro
   - Add new food item
   - Show expiry tracking

3. **Food Bank Workflow** (90 seconds)
   - Login as cityfoodbank
   - Browse available food
   - Submit donation request

4. **Approval Process** (60 seconds)
   - Switch back to restaurant
   - Approve the request
   - Show status updates

5. **AI Meal Planner** (60 seconds)
   - Login as individual
   - Generate AI recipe
   - Show detailed instructions

6. **Analytics Impact** (30 seconds)
   - Show environmental impact
   - Platform-wide statistics

**Your FoodSaver platform is now ready for comprehensive testing and demonstration!** 🚀
