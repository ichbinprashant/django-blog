from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # Fields to be included in the form
        fields = ['title', 'content'] #removing author from the field since it will be by default the user

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        # Fields for user registration
        fields = ['username', 'email', 'password1', 'password2']