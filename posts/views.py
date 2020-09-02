from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post


def index(request):
    post = Post.objects.all()
    return render(request, 'users/home.html', {'post': post})


# creating index with  generic views
class PostListView(ListView):
    model = Post
    template_name = 'users/home.html'
    context_object_name = 'post'
    ordering = ['-date_published']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'blog_post']

    def form_valid(self, form):  # saves the form with the details provided by the user
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'blog_post']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):  # use this function to prevent a user from updating someone else post
        post = self.get_object()  # get the current post that want to be updated
        if self.request.user == post.user:  # check if the login user is the owner of the post
            return True  # update post if condition is true
        return False  # returns 403 forbidden


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False


class PostLatestView(ListView):
    model = Post
    template_name = 'posts/latest_posts.html'
    context_object_name = 'post'
    queryset = Post.objects.order_by('-date_published')[:2]


#  function for about page
def about(request):
    return render(request, 'users/about.html')
