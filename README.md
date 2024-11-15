Calorie Tracker Created by Rohit Mukkemwar.
This is a simple Django web application to track daily calorie intake. Users can add new calorie entries for food items, view past entries, and see a summary of total calories consumed.

Features
Add New Calorie Entry: A form to input the food item, calorie count, and date.
View Past Entries: Displays a list of previous calorie entries with dates, food items, and calories consumed.
Total Calorie Calculation: Summarises total calories consumed.

Requirements:
Python 3.x
Django 4.x

Installation
Clone the repository:
git clone <repository_url>
cd CalorieTracker

Create a virtual environment:
python -m venv djangoenv
source djangoenv/bin/activate  # On Windows: djangoenv\Scripts\activate

Install dependencies:
pip install django

Apply migrations:
python manage.py makemigrations
python manage.py migrate

Create a superuser (optional, for admin access):
python manage.py createsuperuser

Usage
Run the development server:
python manage.py runserver
Access the application: Visit http://127.0.0.1:8000/ to view the calorie tracker home page.

Admin Panel (Optional): If you created a superuser, visit http://127.0.0.1:8000/admin to access the admin interface.

Code Overview
models.py: Defines the CalorieEntry model with fields for date, food item, and calories.
forms.py: Defines a form for adding new calorie entries.
views.py: Contains views for the homepage, which handles both form submission and display of past entries.
home.html: HTML template that displays the form, total calories, and past entries in a styled layout.
Built With
Django - The web framework used
HTML & CSS - For structuring and styling the frontend
Future Improvements
User authentication for personalized calorie tracking.
Graphs and charts to visualize calorie intake trends.
Filtering and sorting options for entries.
