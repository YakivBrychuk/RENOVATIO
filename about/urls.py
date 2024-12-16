from django.urls import path
from . import views

# Define URL patterns for the app
urlpatterns = [
    # URL pattern for the "About Me" page
    path('', views.about_me, name='about'),
]
