from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username','email',]
        # fields = UserCreationForm.Meta.fields
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['username','email', 'password']
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('nickname','introduction','year_of_birth','favorite_genre')
        BIRTH_YEAR_CHOICE = (('1998','1998'),('1999','1999'),('2000','2000'),('2001','2001'),('2002','2002'),('2003','2003'),
            ('2004','2004'),('2005','2005'),('2006','2006'),('2007','2007'),('2008','2008'),('2009','2009'),('2010','2010'),
            ('2011','2011'),('2012','2012'),('2013','2013'),('2014','2014'),('2015','2015'),('2016','2016'),('2017','2017'),
            ('2018','2018'),('2019','2019'),)
        FAVORITE_GENRE_CHOICE = (
            ('공포','공포'),('느와르','느와르'),('다큐멘터리','다큐멘터리'),('드라마','드라마'),
            ('멜로/로맨스','멜로/로맨스'),('모험','모험'),('뮤지컬','뮤지컬'),('미스터리','미스터리'),('범죄','범죄'),
            ('서사','서사'),('스릴러','스릴러'),('애니메이션','애니메이션'),('액션','액션'),
            ('전쟁','전쟁'),('코미디','코미디'),('판타지','판타지'),('한국','한국'),('SF','SF')
            )
            
        widgets = {
            'introduction': forms.Textarea,
            'year_of_birth': forms.Select(choices=BIRTH_YEAR_CHOICE),
            'favorite_genre': forms.Select(choices=FAVORITE_GENRE_CHOICE),
        }

        