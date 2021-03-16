from django.shortcuts import render
from .models import 

# Create your views here.


def shop(request):
    return render(request, 'products/shop.html')


def Ptrainers(request):
    return render(request, 'products/trainers.html')