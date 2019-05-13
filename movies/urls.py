from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('new/', views.new, name='new'), 
    path('<int:movie_pk>/comment/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'), 
    path('<int:movie_pk>/comment/', views.comment_create, name='comment_create'), 
    path('<int:movie_pk>/', views.movie_detail, name='movie_detail'), 
    path('', views.list, name="list"),
    ]