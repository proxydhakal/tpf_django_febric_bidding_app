from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.conf import settings
from PIL import Image
from django.dispatch import receiver
from django.db.models.signals import  post_save



class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    profile_image=models.ImageField(default='default.jpg',upload_to='profile_pics/')
    

    def __str__(self):
        return self.user.username


    def save(self, *args, **kawrgs):
        super().save(*args, **kawrgs)

        img = Image.open(self.profile_image.path)

        if img.height > 300 or img.width> 300:
            output_size =(300,300)
            img.thumbnail(output_size)
            img.save(self.profile_image.path)
        else:
            img.save(self.profile_image.path)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()