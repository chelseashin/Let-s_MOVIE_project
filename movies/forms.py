from .models import Movie, Comment
from django import forms



class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['rank', 'title', 'release_year', 'audience', 'nationality', 'distributor', 'score', 'director', 'actors', 'genre',
        'running_time', 'grade', 'story', 'poster_url']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content',]