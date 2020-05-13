from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from .models import Profile,User

@receiver(post_save,sender=User)
def user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)