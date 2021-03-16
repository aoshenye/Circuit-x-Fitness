from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from shop.views import shop
from trainers.views import Ptrainers 

urlpatterns = [
    path('trainers', Ptrainers, name='Ptrainers'),
    path('shop/', views.shop, name='shop')
]
