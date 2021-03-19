from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_trainers, name='trainers'),
    #path('<product_id>', views.product_detail, name='product_detail')
]
