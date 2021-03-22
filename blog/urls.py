from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.PostList.as_view(), name='profile'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('profile', views.profile, name='profile'),
    path('signin', views.signin, name='signin'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('profile_index', views.profile_index, name='profile_index'),
    path('<slug:slug>/', views.post_detail, name='post_detail')
]