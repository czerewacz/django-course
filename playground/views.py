from django.shortcuts import render
from django.http import HttpResponse

# Note: In storefront/urls.py, the 'include' import was added to reference playground/urls.py.
# This allows Django to route requests to the playground app's URL patterns.


def say_hello(request):
    # You can use named (keyword) arguments in Python, similar to Kotlin
    return render(
        request=request, template_name="hello.html", context={"name": "Django Learner"}
    )
