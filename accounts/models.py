from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser 

# Create your models here.  
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=10, blank=True)
    introduction = models.TextField(blank=True)
    year_of_birth = models.TextField(blank=True)
    favorite_genre = models.CharField(max_length=40, blank=True)
    
class User(AbstractUser):
    # AbstractUser 상속받음
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings')