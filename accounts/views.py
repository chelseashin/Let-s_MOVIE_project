import hashlib
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm, ProfileForm
from .models import Profile, User

# Create your views here.
# 회원가입
def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:list')

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            auth_login(request, user)
            return redirect('accounts:profile')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form, 
    }
    return render(request, 'accounts/auth_form.html', context)
    
# 로그인
def login(request):
    if request.user.is_authenticated:
        return redirect('movies:list')
        
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'movies:list')
    else: 
        form = AuthenticationForm()
    context = {
        'form' : form, 
    }
    return render(request, 'accounts/auth_form.html', context)
    
# 로그아웃
def logout(request):
    auth_logout(request)
    return redirect('movies:list')
    
# 회원정보수정
@login_required
def update(request):
    if request.method == 'POST':
        user_change_form = CustomUserChangeForm(request.POST, instance=request.user)
        if user_change_form.is_valid():
            user_change_form.save()
            return redirect('accounts:user_profile', request.user)
    else:
        user_change_form = CustomUserChangeForm(instance=request.user)
    context = {
        'form' : user_change_form,
    }
    return render(request, 'accounts/auth_form.html', context)

#비밀번호 변경
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            auth_login(request, request.user)
            return redirect('accounts:user_profile', request.user.username)
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/auth_form.html', context)
    
# 회원탈퇴
@login_required
def delete(request):
    if request.method == 'POST':
        request.user.delete()
    return redirect('movies:list')

# 프로필 1:1
@login_required
def profile(request):
    profile = Profile.objects.get_or_create(user=request.user) 
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('accounts:user_profile', request.user)
    else:
        form = ProfileForm(instance = request.user.profile)
    context = {'form': form, }
    return render(request, 'accounts/auth_form.html', context)
    
# 유저페이지
def user_profile(request, user_name):
    people = get_object_or_404(get_user_model(), username=user_name)
    context = {'people': people,}
    return render(request, 'accounts/people.html', context)
    
# 팔로우
@login_required
def follow(request, user_pk):
    people = get_object_or_404(get_user_model(), pk=user_pk)
    if request.user in people.followers.all():
        people.followers.remove(request.user)
    else:
        people.followers.add(request.user)
    return redirect('accounts:user_profile', people.username)
    
# followings
@login_required
def followings(request):
    
    profiles = Profile.objects.filter(user__in = request.user.followings.all()).order_by('-pk')
    context={
        'profiles': profiles,
    }
    
    return render(request, 'accounts/followings.html',context)