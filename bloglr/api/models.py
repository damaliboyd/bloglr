from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OnetoOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=750, blank=True)
    location = models.CharField(max_length=50, blank=True)
    birth_date = models.DateField(null=True,blank=True)post = models.ForiegnKey(Post, on_delete=models.CASCADE)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwards):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, created, **kwargs):
    instance

class Post(models.Model):
    user = models.ForiegnKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

class Comment(models.Model):
    post = models.ForiegnKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    author = models.CharField(max_length=50)
    created = models.DateField(auto_now_add=True)
