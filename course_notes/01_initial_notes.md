# First commands: 
pipenv install django  # Install Django using pipenv
pipenv shell           # Activate the pipenv virtual environment
django-admin startproject config .  # Create a new Django project named 'config' in the current directory


# Run Server
python manage.py runserver 

Open http://127.0.0.1:8000/ on a browser :) 


# Use the terminal inside VSCode
- pipenv --venv gill give u the path for the environment.


In VSCODE select interpreter python and choose enter interpreter path:
/Users/{username}}/.local/share/virtualenvs/storefront-HT1tHN07/bin/python

Then you can run the server from VS Console

# Setting.py
Django is a collection of apps that you can see installed apps in settings.py
INSTALLED_APPS = [
    'django.contrib.admin',        # Admin site
    'django.contrib.auth',         # Authentication system
    'django.contrib.contenttypes', # Content type framework
    'django.contrib.sessions',     # Session management (Legacy), can be deleted
    'django.contrib.messages',     # Messaging framework
    'django.contrib.staticfiles',  # Static file management
]
    
# Django App Structure: playground
When you run `python manage.py startapp playground`, Django creates a folder with several files:

- `__init__.py`: Marks the directory as a Python package.
- `admin.py`: Register models to appear in the Django admin site.
- `apps.py`: App configuration settings.
- `models.py`: Define your database models here.
- `tests.py`: Write tests for your app here.
- `views.py`: Handle the logic for requests and responses. (Is not a view)
- `migrations/`: Store migration files for database schema changes.

This represents a django app that always will have a structure like this
An app is a self-contained module that does one thing (users, blog, payments, API, etc.).

🔹 If you’re building an API

Yes — you would usually make a Django app for your API. For example:
Project: storefront (overall ecommerce site)
Apps inside:
 - catalog (products, categories)
 - cart (shopping cart)
 - orders (checkout, payments)
 - api (if you want to group your REST API logic separately, though often you add API views inside each app)

If you use Django REST Framework (DRF), you might:
Create an app called api and put your serializers/views/urls there, OR
Add API views directly inside each functional app (e.g., orders/api.py).


Important: After creating an app you need to add it to installed apps :D 