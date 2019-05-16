from django.contrib import admin
from .models import Movie, Actor
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id','rank', 'title', 'release_year', 'audience', 'nationality',]
    # 'distributor', 'score', 'director', 'actor1', 'actor2', 'actor3', 'genre', 'running_time', 'grade', 'story', 'poster_url']
    # list_display = '__all__'
admin.site.register(Movie, MovieAdmin)

class ActorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]
admin.site.register(Actor, ActorAdmin)

# rank, title, release_date, audience, nationality, distributor, score, director, actor1, actor2, actor3, genre, running_time, grade, story, poster_url										