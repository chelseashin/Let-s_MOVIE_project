# Create your models here.
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Actor(models.Model):
    name = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class Movie(models.Model):
    rank = models.IntegerField(blank=True)
    title = models.TextField(blank=True)
    release_year = models.TextField(blank=True)
    audience = models.IntegerField(blank=True)
    nationality = models.TextField(blank=True)
    distributor = models.TextField(blank=True)
    score = models.IntegerField(blank=True)
    director = models.TextField(blank=True)
    actors = models.ManyToManyField(Actor, related_name='movies', blank=True)
    genre = models.TextField(blank=True)
    running_time = models.TextField(blank=True)
    grade = models.TextField(blank=True)
    story = models.TextField(blank=True)
    poster_url = models.TextField(blank=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_movies", blank=True)
    
    def __str__(self):
        return self.title
        
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    score = models.IntegerField(blank=True)
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.content