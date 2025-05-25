"""
Django forms for the Food Waste Reduction Platform
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, FoodItem, DonationRequest, MealPlan, FoodCategory


class CustomUserCreationForm(UserCreationForm):
    """Extended user registration form"""
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=False)
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=False)
    organization_name = forms.CharField(max_length=200, required=False)
    role = forms.ChoiceField(choices=User.ROLE_CHOICES)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'role', 
                 'phone', 'address', 'organization_name')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class FoodItemForm(forms.ModelForm):
    """Form for adding/editing food items"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ensure categories are properly loaded
        self.fields['category'].queryset = FoodCategory.objects.all()
        self.fields['category'].empty_label = "Select a category"
        
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
    
    class Meta:
        model = FoodItem
        fields = ['name', 'category', 'description', 'quantity', 'unit', 'expiry_date', 
                 'image', 'pickup_location', 'special_instructions']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'expiry_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'pickup_location': forms.Textarea(attrs={'rows': 2}),
            'special_instructions': forms.Textarea(attrs={'rows': 2}),
        }


class DonationRequestForm(forms.ModelForm):
    """Form for requesting food donations"""
    class Meta:
        model = DonationRequest
        fields = ['requested_quantity', 'message', 'pickup_time']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 3}),
            'pickup_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class MealPlanForm(forms.ModelForm):
    """Form for creating meal plans manually"""
    class Meta:
        model = MealPlan
        fields = ['title', 'description', 'ingredients', 'instructions', 'servings', 'prep_time']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'ingredients': forms.Textarea(attrs={'rows': 4}),
            'instructions': forms.Textarea(attrs={'rows': 5}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class AIIngredientForm(forms.Form):
    """Form for AI-powered meal planning"""
    ingredients = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 4, 
            'placeholder': 'Enter available ingredients (e.g., chicken breast, rice, tomatoes, onions)',
            'class': 'form-control'
        }),
        help_text="List the ingredients you have available, separated by commas"
    )
    dietary_preferences = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'e.g., vegetarian, gluten-free, low-carb',
            'class': 'form-control'
        })
    )
    servings = forms.IntegerField(
        min_value=1,
        max_value=10,
        initial=2,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )


class WastePredictionForm(forms.Form):
    """Form for AI waste prediction analysis"""
    food_type = forms.ModelChoiceField(
        queryset=FoodCategory.objects.all(),
        empty_label="Select food category",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    analysis_period = forms.ChoiceField(
        choices=[
            ('week', 'Next Week'),
            ('month', 'Next Month'),
            ('season', 'Next Season'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    include_suggestions = forms.BooleanField(
        required=False,
        initial=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
