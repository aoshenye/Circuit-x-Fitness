from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.

def index(request):
    """ A view to return the index page """
    
    return render(request, 'home/index.html')

def about_us(request):
    return render(request,'home/about_us.html')


def products(request):
    return render(request, '/products.html')


