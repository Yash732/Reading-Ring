#This code defines URL patterns for a Django application named "item". Specifically, it maps a URL to a view function, which will handle the logic when a user visits that URL.
#app_name is set to 'item', which is used for namespacing URLs in this Django application. This is helpful when you have multiple apps in your project and want to ensure URL names are unique across the project.
#name='detail' assigns a name to this URL pattern, which can be used to refer to this URL in templates and other parts of your Django project.
from django.urls import path
from . import views

app_name = 'item'

#pk (integer) has to be same as set in views.py of item folder
#next Step: import this file in main urls.py
urlpatterns = [
    path('<int:pk>/',views.detail, name = 'detail'),
    path('jew/', views.new, name = 'new'),
]