# Django Views
Views in Django are Python functions or classes that handle HTTP requests and return HTTP responses. They contain the logic for processing user input, interacting with models, and rendering templates(views in Django).

## Example: Simple Function-Based View
```python
def hello(request):
    return HttpResponse('Hello, world!')
```
This view receives a `request` object and returns a plain text response.

# Mapping Views to URLs
To make a view accessible, you need to map it to a URL pattern in your Django app's `urls.py` file. This tells Django which view to call when a user visits a specific URL.

## Example: Mapping the `hello` view
```python
from django.urls import path
from .views import hello

urlpatterns = [
    path('hello/', hello),
]
```
Now, visiting `/hello/` in your browser will trigger the `hello` view and display "Hello, world!".

# Linking App URLs in Project
To connect your app's URLs to the main project, you need to use the `include` function in your project's `urls.py` (usually in the `storefront` folder). This lets Django route requests to your app's URL patterns.

## Example: storefront/urls.py
```python
from django.contrib import admin
from django.urls import path, include  # include lets you reference app URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('playground/', include('playground.urls')),
]
```
Now, any request to `/playground/` will be handled by the URL patterns defined in `playground/urls.py`.

