"""
Test cases for the Food Waste Reduction Platform
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import FoodCategory, FoodItem

User = get_user_model()


class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123',
            role='contributor'
        )
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.role, 'contributor')


class FoodItemModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123',
            role='contributor'
        )
        self.category = FoodCategory.objects.create(
            name='Test Category',
            description='Test description'
        )
    
    def test_create_food_item(self):
        from django.utils import timezone
        from datetime import timedelta
        
        food_item = FoodItem.objects.create(
            contributor=self.user,
            name='Test Food',
            category=self.category,
            description='Test description',
            quantity=10,
            unit='pieces',
            expiry_date=timezone.now() + timedelta(days=3),
            pickup_location='Test location'
        )
        
        self.assertEqual(food_item.name, 'Test Food')
        self.assertEqual(food_item.contributor, self.user)
