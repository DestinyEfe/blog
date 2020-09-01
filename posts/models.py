from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from formview.models import Profile


# create models here


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    blog_post = models.TextField(max_length=600, default='')
    date_published = models.DateTimeField('publication_date', auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.user} Post'

    # redirect to post_detail url if post is created
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
