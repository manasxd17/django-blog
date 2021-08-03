from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from .models import blog_post

class Signup(UserCreationForm):
    class Meta:
        password1 = forms.CharField(label = 'Password', widget = forms.PasswordInput())
        password2 = forms.CharField(label = 'Confirm Password', widget = forms.PasswordInput())
        model = User
        fields = ['username','email']

class login_user(AuthenticationForm):
    username = UsernameField()
    password = forms.CharField(widget = forms.PasswordInput())

class add_blog(forms.ModelForm):
    class Meta:
        model = blog_post
        fields = ['title','desc']
        labels = {'title':'Title','desc':'Description'}