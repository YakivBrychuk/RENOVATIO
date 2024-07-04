from django.urls import path
from . import views


# Path: blog/urls.py
urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
]