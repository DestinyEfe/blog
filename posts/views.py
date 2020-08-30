from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import PostCreationForm
from users.models import Post
# Create your views here.

@login_required
def posts(request):
    if request.method == "POST":
        form = PostCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('name')
            occupation = form.cleaned_data.get('occupation')
            user_detail = Post(users=username, occupation=occupation)
            user_detail.save()
            messages.success(request, f'Successfully Posted your information')
            return redirect('posts')
    else:
        form = PostCreationForm()
    return render(request, 'posts/post.html', {'form':form})


def users_link(request, username):
    user_page_link = get_object_or_404(User, username=username)
    return render(request, 'posts/user_page.html', {'user_page_link':user_page_link}) 
