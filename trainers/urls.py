from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_trainers, name='trainers'),
    path('<trainer_id>', views.trainer_detail, name='trainer_detail')
]
