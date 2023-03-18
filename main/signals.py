from django.db.models.signals import post_save, pre_delete
# from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import User


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print(1234)
    if created:
        User.objects.update(key_aes='12312')


# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     instance.profile.save()