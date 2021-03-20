from django.views import generic
from .models import Post
from .forms import NewUserForm, UserLoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.core.mail import EmailMessage





class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'profile.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


@login_required()
def profile(request):
    return (request,'blog/profile.html')


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
    return render(request,'blog/signin.html', locals())

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
        return render(request, 'blog/sign_up.html', context)