"""
URL patterns for the FoodApp
"""
from django.urls import path
from . import views

urlpatterns = [
    # Home and authentication
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Food Items Management
    path('add-food/', views.add_food_item, name='add_food_item'),
    path('my-food/', views.my_food_items, name='my_food_items'),
    path('available-food/', views.available_food, name='available_food'),
    
    # Donation Management
    path('request-donation/<int:food_item_id>/', views.request_donation, name='request_donation'),
    path('my-requests/', views.my_requests, name='my_requests'),
    path('manage-requests/', views.manage_requests, name='manage_requests'),
    path('approve-request/<int:request_id>/', views.approve_request, name='approve_request'),
    
    # Meal Planning
    path('ai-meal-planner/', views.ai_meal_planner, name='ai_meal_planner'),
    path('meal-plans/', views.meal_plans, name='meal_plans'),
    path('meal-plan/<int:plan_id>/', views.meal_plan_detail, name='meal_plan_detail'),
    
    # AI Features
    path('waste-prediction/', views.waste_prediction, name='waste_prediction'),
    
    # Analytics & Notifications
    path('analytics/', views.analytics, name='analytics'),
    path('notifications/', views.notifications, name='notifications'),
    
    # API Endpoints
    path('api/food-items/', views.api_food_items, name='api_food_items'),
]
