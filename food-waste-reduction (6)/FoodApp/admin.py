"""
Django admin configuration
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, FoodCategory, FoodItem, DonationRequest, MealPlan, WasteAnalytics, Notification


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'organization_name', 'is_verified', 'date_joined')
    list_filter = ('role', 'is_verified', 'is_active')
    search_fields = ('username', 'email', 'organization_name')
    
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {
            'fields': ('role', 'phone', 'address', 'latitude', 'longitude', 
                      'organization_name', 'is_verified')
        }),
    )


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'description')
    search_fields = ('name',)


@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'contributor', 'category', 'quantity', 'unit', 
                   'expiry_date', 'status', 'urgency', 'created_at')
    list_filter = ('status', 'urgency', 'category', 'created_at')
    search_fields = ('name', 'contributor__username', 'contributor__organization_name')
    date_hierarchy = 'created_at'


@admin.register(DonationRequest)
class DonationRequestAdmin(admin.ModelAdmin):
    list_display = ('food_item', 'recipient', 'requested_quantity', 'status', 
                   'pickup_time', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('food_item__name', 'recipient__username')


@admin.register(MealPlan)
class MealPlanAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'servings', 'prep_time', 'ai_generated', 'created_at')
    list_filter = ('ai_generated', 'created_at')
    search_fields = ('title', 'user__username')


@admin.register(WasteAnalytics)
class WasteAnalyticsAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'food_saved_kg', 'meals_provided', 
                   'co2_reduced_kg', 'money_saved')
    list_filter = ('date',)
    search_fields = ('user__username',)


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'type', 'is_read', 'created_at')
    list_filter = ('type', 'is_read', 'created_at')
    search_fields = ('user__username', 'title')


# Register the custom user admin
admin.site.register(User, CustomUserAdmin)

# Customize admin site
admin.site.site_header = "FoodSaver Admin"
admin.site.site_title = "FoodSaver Admin Portal"
admin.site.index_title = "Welcome to FoodSaver Administration"
