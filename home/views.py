from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NewUserForm, UserLoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.core.mail import EmailMessage
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.template.loader import render_to_string

# Create your views here.

def index(request):
    """ A view to return the index page """
    
    return render(request, 'home/index.html')

def about_us(request):
    return render(request,'home/about_us.html')



def signin(request):
    if request.method == "POST":
        form = UserLoginForm(request, data=request.POST)
        print(form)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active == True:
                    login(request,user)
                    return redirect('profile')
                else:
                    messages.error("Please confirm your email!")
            else:
                messages.error(request,"Invalid username or password")
        else:
            messages.error(request,"Invalid username or password")
    form = UserLoginForm
    return render(request,'home/signin.html', locals())

def sign_up(request):
    form = NewUserForm
    context = {'form' : form}
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = True
            return redirect('signin')
        context = {'form': form}
    return render(request, 'home/sign_up.html', context)

@login_required()
def profile(request):
    return render(request,'home/profile.html')

