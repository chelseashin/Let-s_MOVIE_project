from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('followings/', views.followings, name='followings'),
    path('<int:user_pk>/follow/', views.follow, name='follow'),
    path('password/', views.change_password , name='change_password'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name="update"),
    # mypage
    path('profile/<str:user_name>/', views.user_profile, name="user_profile"),
    # create/update
    path('profile/', views.profile, name="profile"),  
    path('logout/', views.logout, name="logout"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    ]