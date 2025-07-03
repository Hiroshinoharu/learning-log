""" 
Defines URL pattern for accounts
"""

from django.urls import path, include

from . import views

app_name = 'accounts'
urlpatterns = [
    # Include default auth URLs
    path('', include('django.contrib.auth.urls')),
    # URL for user registration
    path('register/', views.register, name='register'),
]