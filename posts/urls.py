from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name='posts'),
    path('<slug:username>/', views.users_link, name='users_page'),
]