from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('post_detail/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('profile', views.profile, name='profile'),
    path('profile/comment/edit/<int:id>',views.comment_edit, name='comment_edit'),
    path('profile/comment/delete/<int:id>',views.comment_destroy, name='comment_destroy'),
    path('signin', views.signin, name='signin'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('profile_index', views.profile_index, name='profile_index'),
    path('post_detail/<slug:slug>/', views.post_detail, name='post_detail')
]