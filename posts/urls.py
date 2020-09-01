from django.urls import path
from . import views

urlpatterns = [
    path('latest_posts/', views.latest_posts, name='latest_posts'),
]