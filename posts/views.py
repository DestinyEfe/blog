from django.shortcuts import render


from .models import Post


# Create your views here.
def latest_posts(request):
    post = Post.objects.order_by('-date_published')[:1]
    return render(request, 'posts/latest_posts.html',{'post':post})

