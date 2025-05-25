from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import timedelta
import json

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Administrator'),
        ('contributor', 'Food Contributor (Restaurant/Grocer)'),
        ('recipient', 'Food Recipient (Charity/Food Bank)'),
        ('individual', 'Individual User'),
    ]
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='individual')
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    organization_name = models.CharField(max_length=200, blank=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"


class FoodCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Food Categories"
        ordering = ['name']
    
    def __str__(self):
        return self.name


class FoodItem(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('reserved', 'Reserved'),
        ('donated', 'Donated'),
        ('expired', 'Expired'),
    ]
    
    URGENCY_CHOICES = [
        ('low', 'Low (3+ days)'),
        ('medium', 'Medium (1-2 days)'),
        ('high', 'High (Today)'),
        ('critical', 'Critical (Expired)'),
    ]
    
    UNIT_CHOICES = [
        ('kg', 'Kilograms'),
        ('g', 'Grams'),
        ('l', 'Liters'),
        ('ml', 'Milliliters'),
        ('pieces', 'Pieces'),
        ('portions', 'Portions'),
        ('boxes', 'Boxes'),
        ('bags', 'Bags'),
    ]
    
    contributor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='food_items')
    name = models.CharField(max_length=200)
    category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE, related_name='food_items')
    description = models.TextField()
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=20, choices=UNIT_CHOICES, default='kg')
    expiry_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    urgency = models.CharField(max_length=20, choices=URGENCY_CHOICES, default='low')
    image = models.ImageField(upload_to='food_images/', blank=True, null=True)
    pickup_location = models.TextField()
    special_instructions = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.contributor.organization_name or self.contributor.username}"
    
    def days_until_expiry(self):
        """Calculate days until expiry"""
        if self.expiry_date:
            delta = self.expiry_date - timezone.now()
            return delta.days
        return 0
    
    def save(self, *args, **kwargs):
        # Auto-set urgency based on expiry date
        days_left = self.days_until_expiry()
        if days_left < 0:
            self.urgency = 'critical'
            self.status = 'expired'
        elif days_left == 0:
            self.urgency = 'high'
        elif days_left <= 2:
            self.urgency = 'medium'
        else:
            self.urgency = 'low'
        
        super().save(*args, **kwargs)


class DonationRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE, related_name='donation_requests')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='donation_requests')
    requested_quantity = models.DecimalField(max_digits=10, decimal_places=2)
    message = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    pickup_time = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Request for {self.food_item.name} by {self.recipient.username}"


class MealPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meal_plans')
    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    servings = models.IntegerField(default=2)
    prep_time = models.IntegerField(help_text="Preparation time in minutes")
    ai_generated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.title} - {self.user.username}"


class Notification(models.Model):
    TYPE_CHOICES = [
        ('system', 'System'),
        ('donation_request', 'Donation Request'),
        ('expiry_alert', 'Expiry Alert'),
        ('ai_prediction', 'AI Prediction'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=200)
    message = models.TextField()
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='system')
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.title} - {self.user.username}"


class WasteAnalytics(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='waste_analytics')
    date = models.DateField(auto_now_add=True)
    food_saved = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    co2_reduced = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    money_saved = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return f"Analytics for {self.user.username} - {self.date}"


# AI-related models
class FoodWastePrediction(models.Model):
    contributor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='waste_predictions')
    food_category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
    predicted_waste_date = models.DateField()
    predicted_quantity = models.DecimalField(max_digits=10, decimal_places=2)
    confidence_score = models.DecimalField(max_digits=3, decimal_places=2)
    historical_pattern = models.TextField()  # JSON data
    ai_suggestions = models.TextField()  # JSON data
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Prediction for {self.contributor.organization_name} - {self.food_category.name}"
    
    def get_suggestions(self):
        try:
            return json.loads(self.ai_suggestions)
        except:
            return []


class SmartAlert(models.Model):
    ALERT_TYPES = [
        ('waste_prediction', 'Waste Prediction'),
        ('demand_spike', 'Demand Spike'),
        ('optimal_timing', 'Optimal Timing'),
        ('recipient_match', 'Recipient Match'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='smart_alerts')
    alert_type = models.CharField(max_length=20, choices=ALERT_TYPES)
    title = models.CharField(max_length=200)
    message = models.TextField()
    action_data = models.TextField()  # JSON data for actions
    is_active = models.BooleanField(default=True)
    expires_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.title} - {self.user.username}"


class DemandPattern(models.Model):
    food_category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
    day_of_week = models.IntegerField()  # 0=Monday, 6=Sunday
    typical_demand = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ['food_category', 'day_of_week']
    
    def __str__(self):
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        return f"{self.food_category.name} - {days[self.day_of_week]}: {self.typical_demand}"
