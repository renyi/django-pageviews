Introduction
============
A very simple middleware based page view counter. It's sole purpose is to increment page views.


Quickstart
==========
1. Add 'pageviews' to INSTALLED_APPS.
2. Add 'pageviews.middleware.PageViewsMiddleware' to MIDDLEWARE_CLASSES.
3. Run 'python manage.py syncdb' or 'python manage.py migrate'.
4. Add {% load pageviews_tags %} to templates.
5. Insert {% pageviews %} or {% pageviews_url request.path %} to templates.