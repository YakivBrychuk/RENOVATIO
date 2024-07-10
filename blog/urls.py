from . import views
from django.urls import path



# Path: blog/urls.py
urlpatterns = [
    path("", views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]