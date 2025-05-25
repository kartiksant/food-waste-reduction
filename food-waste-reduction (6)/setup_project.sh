#!/bin/bash

echo "Setting up FoodSaver Django Project..."

# Install dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Make migrations
echo "Creating database migrations..."
python manage.py makemigrations FoodApp

# Apply migrations
echo "Applying migrations..."
python manage.py migrate

# Create sample data
echo "Creating sample data..."
python manage.py create_sample_data

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Setup complete!"
echo ""
echo "To start the development server, run:"
echo "python manage.py runserver"
echo ""
echo "Login credentials:"
echo "Admin: admin / admin123"
echo "Restaurant: restaurant1 / restaurant123"
echo "Charity: charity1 / charity123"
