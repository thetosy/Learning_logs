"""defines urls for the user app"""
from django.urls import include, path
from . import views


app_name = 'users'
urlpatterns = [
    # include default django auth
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
]
