from django.urls import path
from richy_cake_app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name="index_page"),
    
]