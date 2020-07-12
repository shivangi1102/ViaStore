from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('register/', views.registervendor),
    path('signin/', views.loginvendor),
    path('product/<int:ven_id>/', views.addproduct),
    path('dashboard/<int:ven_id>/', views.dashboard, name="dashboard"),
    path('logout/', views.logout),

]
