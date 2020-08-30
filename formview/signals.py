from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:  # if user was successfully created
        Profile.objects.create(user=instance)  # create an profile objects for newly created user


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):  # function to save the profile created by the user.
    instance.profile.save()  # save the user profile for the instance created for the user in the third 9th line.think of it as user.profile.save()
