from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name="home"),
    path('login', views.loginUser, name="login"),  # ✅ Updated function name
    path('logout', views.logoutUser, name="logout"),
]
