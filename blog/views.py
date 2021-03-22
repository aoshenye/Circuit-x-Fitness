from django.views import generic
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import NewUserForm, UserLoginForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.core.mail import EmailMessage
from django.http import HttpResponse







class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'profile.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})


def profile_index(request):
    return render(request,'blog/profile_index.html')


@login_required()
def profile(request):
    return render(request,'blog/profile.html')


def signin(request):
    if request.method == "POST":
        form = UserLoginForm(request, data=request.POST)
        print(form)
        if form.is_valid():
            print("Valid")
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                if user.is_active == True:
                    login(request, user)
                    return redirect('profile')
                else:
                    messages.error("Please confirm your email!")
            else:
                messages.error(request,"Invalid username or password")
        else:
            messages.error(request,"Invalid username or password")
    form = UserLoginForm()
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


