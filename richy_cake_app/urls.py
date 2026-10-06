from django.urls import path
from richy_cake_app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name="index_page"),
    path("register/", views.register, name="register"),
    path("login/", views.custom_login, name="login"),
    path("cake/", views.cake_page, name="cake_page"),
    path("add_cake/", views.add_cake, name="add_cake"),
    path("cake_details/<int:pk>/", views.cake_details, name="cake_details"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout")
    
    
]