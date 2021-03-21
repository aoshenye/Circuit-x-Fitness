from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return the index page """
    
    return render(request, 'home/index.html')

def about_us(request):
    return render(request,'home/about_us.html')


def products(request):
    return render(request, '/products.html')


