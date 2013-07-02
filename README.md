Introduction
============
A very simple middleware based page view counter. It's sole purpose is to increment page views.


Quickstart
==========

1. Install from github or clone the repository:
```bash
    pip install git+git://github.com/renyi/django-pageviews.git
```

2. Add 'pageviews' to INSTALLED_APPS.
```python
    INSTALLED_APPS = (
        "...",
        "pageviews",
    )
```

3. Add 'pageviews.middleware.PageViewsMiddleware' to MIDDLEWARE_CLASSES.
```python
    MIDDLEWARE_CLASSES = (
        "...",
        "pageviews.middleware.PageViewsMiddleware"
    )
```

4. Run 'python manage.py syncdb' or 'python manage.py migrate'.
```bash
    python manage.py migrate
```

5. Add {% load pageviews_tags %} to templates.

6. Insert {% pageviews %} or {% pageviews_url request.path %} to templates.
