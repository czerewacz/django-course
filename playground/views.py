from django.shortcuts import render
from django.http import HttpResponse

# Note: In storefront/urls.py, the 'include' import was added to reference playground/urls.py.
# This allows Django to route requests to the playground app's URL patterns.

def say_hello(request):
    return HttpResponse("Hello, world!")
