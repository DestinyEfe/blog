from django.db import models


class Post(models.Model):
    users = models.CharField(max_length=20)
    occupation = models.TextField()

    def __str__(self):
        return self.users
