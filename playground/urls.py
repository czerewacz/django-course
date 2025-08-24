from django.urls import path
from . import views

# Url configuration for the playground app
urlpatterns = [
    path('hello/', views.say_hello, name='say_hello'),
]
