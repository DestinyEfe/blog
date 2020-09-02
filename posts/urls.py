from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views

from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,PostLatestView
from . import views
urlpatterns = [
    path('',PostListView.as_view(),name="index"),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(), name='post_delete'),
    path('post/latest_post/',PostLatestView.as_view(),name="post_latest"),
    path('about/',views.about,name="about_us"),
]