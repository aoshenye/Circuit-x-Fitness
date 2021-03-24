from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render
from blog.models import Whole_comment

# Create your views here.

def index(request):
    """ A view to return the index page """
    comment_all = Whole_comment.objects.filter(active=True).order_by('-created_on')
    return render(request, 'home/index.html',{
        'comment_all': comment_all
    })

def about_us(request):
    return render(request,'home/about_us.html')


def products(request):
    return render(request, '/products.html')


