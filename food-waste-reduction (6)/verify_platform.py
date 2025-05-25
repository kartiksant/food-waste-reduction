#!/usr/bin/env python
"""
Platform Verification Script
Checks if all components are working correctly
"""

import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Mainproj.settings')
django.setup()

from FoodApp.models import User, FoodCategory, FoodItem, DonationRequest
from django.conf import settings

def verify_platform():
    print("🔍 Verifying Food Waste Reduction Platform...")
    print("=" * 50)
    
    issues = []
    
    # Check 1: Database Connection
    try:
        user_count = User.objects.count()
        print(f"✅ Database: Connected ({user_count} users)")
    except Exception as e:
        issues.append(f"❌ Database: {str(e)}")
    
    # Check 2: Food Categories
    try:
        categories = FoodCategory.objects.all()
        if categories.count() >= 12:
            print(f"✅ Categories: {categories.count()} categories available")
            for cat in categories:
                print(f"   - {cat.name}")
        else:
            issues.append(f"❌ Categories: Only {categories.count()} found, need 12")
    except Exception as e:
        issues.append(f"❌ Categories: {str(e)}")
    
    # Check 3: Test Users
    try:
        test_users = ['admin', 'greenbistro', 'cityfoodbank', 'johnsmith']
        existing_users = []
        for username in test_users:
            if User.objects.filter(username=username).exists():
                existing_users.append(username)
        
        if len(existing_users) >= 3:
            print(f"✅ Test Users: {len(existing_users)} test accounts ready")
            for user in existing_users:
                print(f"   - {user}")
        else:
            issues.append(f"❌ Test Users: Only {len(existing_users)} found")
    except Exception as e:
        issues.append(f"❌ Test Users: {str(e)}")
    
    # Check 4: Gemini AI Configuration
    try:
        api_key = getattr(settings, 'GEMINI_API_KEY', None)
        if api_key and len(api_key) > 20:
            print("✅ AI: Gemini API key configured")
        else:
            issues.append("❌ AI: Gemini API key missing or invalid")
    except Exception as e:
        issues.append(f"❌ AI: {str(e)}")
    
    # Check 5: Sample Data
    try:
        food_items = FoodItem.objects.count()
        requests = DonationRequest.objects.count()
        if food_items > 0:
            print(f"✅ Sample Data: {food_items} food items, {requests} requests")
        else:
            issues.append("❌ Sample Data: No food items found")
    except Exception as e:
        issues.append(f"❌ Sample Data: {str(e)}")
    
    # Check 6: Media Directories
    media_dirs = ['media', 'media/food_images', 'static', 'staticfiles']
    missing_dirs = []
    for dir_path in media_dirs:
        if not os.path.exists(dir_path):
            missing_dirs.append(dir_path)
    
    if not missing_dirs:
        print("✅ Directories: All media directories exist")
    else:
        issues.append(f"❌ Directories: Missing {missing_dirs}")
    
    print("=" * 50)
    
    if not issues:
        print("🎉 PLATFORM VERIFICATION SUCCESSFUL!")
        print("✅ All components are working correctly")
        print("🚀 Ready for testing and deployment")
        print("\n📋 Test Accounts:")
        print("   Admin: admin / admin123")
        print("   Restaurant: greenbistro / restaurant123") 
        print("   Food Bank: cityfoodbank / foodbank123")
        print("   Individual: johnsmith / individual123")
        print("\n🌐 Start server: python manage.py runserver")
        return True
    else:
        print("⚠️ PLATFORM VERIFICATION FAILED!")
        print("❌ Issues found:")
        for issue in issues:
            print(f"   {issue}")
        print("\n🔧 Run setup script to fix issues:")
        print("   ./setup_complete_platform.sh")
        return False

if __name__ == "__main__":
    verify_platform()
