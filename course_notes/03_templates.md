# Templates

# Django Templates Introduction
Templates in Django are used to separate the presentation layer (HTML) from the business logic (Python code). They allow you to generate dynamic HTML pages by embedding variables and logic directly in your HTML files.

## Why Use Templates?
- Keep your code organized and maintainable
- Reuse HTML structures across multiple pages
- Easily display data from your views and models

## How Templates Work
1. You create HTML files with special Django template tags and variables.
2. Your view passes data to the template.
3. Django renders the template and returns the final HTML to the browser.

## Example
Suppose you have a template called `hello.html`:
```html
<h1>Hello, {{ name }}!</h1>
```
And a view:
```python
def say_hello(request):
    return render(request, 'hello.html', {'name': 'World'})
```
This will display "Hello, World!" in the browser.

---

## Final Note: Modern Django Usage
While Django templates are powerful for server-rendered HTML, most modern web development uses Django primarily for building APIs. This is because:
- Frontend frameworks (like React, Vue, Angular) handle the user interface and dynamic content.
- APIs (using Django REST Framework or similar) provide data to these frontends via JSON.

Django templates are still useful for simple sites, but for scalable and interactive applications, separating backend (API) and frontend is now the standard approach.

