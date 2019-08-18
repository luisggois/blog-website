from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


''' 
- post-save signal is triggered once an object is saved (in this case when an user get's created)
- User model will be the sender who sends the signal!
- Receiver is a function that get's the signal and performs certains tasks 
'''


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
