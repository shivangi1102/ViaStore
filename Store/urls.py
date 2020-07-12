from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('login/', views.login1),
    path('', views.index),
    path('homepage/', views.user_login),
    path('productdetail/<int:id>/', views.product, name='product'),
    path('logout/', views.logout),
    url(r'^cartdetail/$', views.cart_detail, name='cart_detail'),
    url(r'^add/(?P<product_id>\d+)/$', views.cart_add, name='cart_add'),
    url(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'),
    url(r'^create/$', views.order_create, name='order_create')
]
