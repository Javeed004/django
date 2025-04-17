from django.contrib import admin
from django.urls import path
from kct import views

urlpatterns = [
    path('loginpage/', views.loginPage, name='loginpage'),
    path('newview/', views.newView, name='newview'),
]