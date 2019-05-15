from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('all_movie/', views.all_movie, name='all_movie'),
    path('click_keyword/<str:category>/<str:word>/', views.click_keyword, name='click_keyword'), 
    path('search/', views.search, name='search'), 
    path('<int:movie_pk>/like/', views.like, name='like'), 
    path('new/', views.new, name='new'), 
    path('<int:movie_pk>/comment/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'), 
    path('<int:movie_pk>/comment/', views.comment_create, name='comment_create'), 
    path('<int:movie_pk>/', views.movie_detail, name='movie_detail'), 
    path('', views.list, name="list"),
    ]