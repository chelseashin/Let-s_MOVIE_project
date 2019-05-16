import js2py
from js2py import require
from npm.finders import npm_install
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http import JsonResponse, HttpResponseBadRequest
from django.contrib import messages
from .forms import CommentForm, MovieForm
from .models import Movie, Comment, Actor
from accounts.models import Profile

# Create your views here.
def list(request):
    top_ten = Movie.objects.all()[0:10]
    if request.user.is_authenticated or request.user.is_superuser:
        comment = Comment.objects.filter(user_id=request.user.id, score__gte=6)
        context.update(dict(commet=comment))
        print(comment)
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
        
   
    # data = []
    # for movie in all_movie:
    #     for comment in movie.comment_set.all():
    #         data.append({'movie_id':str(movie.id), 'user_id':str(comment.user_id),'rating':str(comment.score)})
    # js2py.translate_file('example.js', 'example.py')
    
    # from example import example
    p
    
    
    return render(request, 'movies/list.html', context)
    
# 모든 영화보기 25개씩 pagination
def all_movie(request):
    movie_list = Movie.objects.all()
    paginator = Paginator(movie_list, 24)
    page = request.GET.get('page')
    movies = paginator.get_page(page)
    context = {
        'movies' : movies, 
    }
    return render(request, 'movies/movie_list.html', context)
    
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
    print(movie.actors.all)
    # movie = Movie.objects.get(pk=movie_pk)
    comment_form = CommentForm()
    context = {
        'movie' : movie, 
        'comment_form' : comment_form, 
    }
    return render(request, 'movies/movie_detail.html', context)
    
# 댓글
@require_POST
@login_required
def comment_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if len(movie.comment_set.filter(user_id = request.user.id)) == 0:
        comment_form = CommentForm(request.POST)
        score = request.POST.get('star')
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user_id = request.user.pk
            comment.score = score
            # comment.user = request.user
            comment.movie_id = movie_pk
            comment.save()
        return redirect('movies:movie_detail', movie_pk)
    else:
        messages.add_message(request, messages.WARNING, "이미 댓글을 작성 하셨습니다.")
        return redirect('movies:movie_detail', movie_pk)
 
@login_required
def comment_update(request, comment_pk):
    comment  = get_object_or_404(Comment, pk=comment_pk)
    if request.method == "POST":
        form = CommentForm(instance=comment, data=request.POST)
        if form.is_valid():
            score = request.POST.get('star')
            comment = form.save(commit=False)
            comment.score = score
            comment.save()
            return redirect('movies:movie_detail', comment.movie_id )
    else:
        form = CommentForm(instance=comment)
    context = {
        'form':form,
        'comment':comment
    }
    return render(request, 'movies/forms.html', context)
 
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
        
@login_required
def search(request):
    category = request.GET.get('category')
    word = request.GET.get('word')
    # print(category)
    
    if category == '영화 제목':
        movies =  Movie.objects.filter(title=word)
    elif category == '영화 감독':
        movies =  Movie.objects.filter(director=word)
    elif category == '영화 배우':
        actor =  Actor.objects.get(name=word)
        movies = actor.movies.all
        print(movies)
    elif category == '영화 장르':
        movies =  Movie.objects.filter(genre=word)
    context = {
        'category':category,
        'word':word,
        'movies':movies,
    }
    return render(request, 'movies/search_movie.html',context)
    
def click_keyword(request, category, word):
    if category == '영화 감독':
        movies =  Movie.objects.filter(director=word)
    elif category == '영화 배우':
        actor =  Actor.objects.get(name=word)
        movies = actor.movies.all
        print(movies)
    elif category == '영화 장르':
        movies =  Movie.objects.filter(genre=word)
    context = {
        'category':category,
        'word':word,
        'movies':movies,
    }
    return render(request, 'movies/search_movie.html',context)
  

    