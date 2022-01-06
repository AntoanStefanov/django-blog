# sender
from django.contrib.auth.models import User
# signal
from django.db.models.signals import post_save
# reciever
from django.dispatch import reciever

# profile model to create a profile in the reciever(the function)
from .models import Profile

# post_save signal when a user is created.
# User model here is what we call the sender,
# since is what is going to send the signal.
# We need a reciever, it's going to be a function
# that gets this signal and then perform some task

# we want to run this function every time a user is created.
# https://youtu.be/FdVuKt_iuSI?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&t=1832
@reciever(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@reciever(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()