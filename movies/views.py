from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
from .forms import CommentForm, MovieForm
from .models import Movie, Comment
from accounts.models import Profile


# Create your views here.
def list(request):
    top_ten = Movie.objects.all()[0:10]
    if request.user.is_authenticated:
        user = get_object_or_404(Profile, user = request.user)
        
        genre_movie = Movie.objects.filter(genre=user.favorite_genre)
        year_movie = Movie.objects.filter(release_year=user.year_of_birth)
        context = {
            'top_ten' : top_ten,
            'genre_movie': genre_movie,
            'year_movie' : year_movie,
        }
    else:
        context = {
            'top_ten' : top_ten,
        }
    return render(request, 'movies/list.html', context)
    
# 영화 등록 - 관리자만 가능
@login_required
def new(request):
    if request.user.is_superuser:
        if request.method == "POST":
            form = MovieForm(request.POST)
            if form.is_valid():
                movie = form.save(commit=False)
                movie.user = request.user
                movie.save()
                return redirect('movies:list')
        else:
            form = MovieForm()
        context = {
            'form': form,
        }
        return render(request, 'movies/forms.html', context)
    else:
        messages.add_message(request, messages.SUCCESS, "관리자만이 삭제가 가능합니다! <a href='/movies/'>홈으로</a>")
        return redirect('movies:list')
    
# 영화 수정 - 관리자만 가능
# def delete(request, post_pk):
#     movie = get_object_or_404(Movie, pk=movie_pk)
#     if request.user.is_superuser:
#         
#         return redirect('movies:movie_detail', movie_pk)

# 영화 삭제 - 관리자만 가능
# def delete(request, post_pk):
#     movie = get_object_or_404(Movie, pk=movie_pk)
#     if request.user.is_superuser:
#         movie.delete()
#         return redirect('movies:list')
    
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    # movie = Movie.objects.get(pk=movie_pk)
    comment_form = CommentForm()
    context = {
        'movie' : movie, 
        'comment_form' : comment_form, 
    }
    return render(request, 'movies/movie_detail.html', context)
    
@require_POST
def comment_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    comment_form = CommentForm(request.POST)
    score = request.POST.get('star')
    print(score)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user_id = request.user.pk
        comment.score = score
        # comment.user = request.user
        comment.movie_id = movie_pk
        comment.save()
    return redirect('movies:movie_detail', movie_pk)
 
@require_POST
@login_required
def comment_delete(request, movie_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user != comment.user:
        return redirect('posts:list')
    comment.delete()
    return redirect('movies:movie_detail', movie_pk)
    
# 좋아요
@login_required
def like(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.user in movie.like_users.all():
        movie.like_users.remove(request.user)
    else:
        movie.like_users.add(request.user)
    return redirect('movies:movie_detail', movie_pk)