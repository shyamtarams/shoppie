from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import myUser

class CustomUserCreationForm(UserCreationForm):
    class meta:
        model = myUser
        field = "__all__"


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    status=forms.CharField(max_length=20)
    rule=forms.CharField(max_length=20)
    class Meta:
        model = myUser
        fields = ('username', 'email', 'password1','password2','status','rule')

class SellerSignUpForm(UserCreationForm):
    name=forms.CharField(max_length=200)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    status = forms.CharField(max_length=20)
    rule=forms.CharField(max_length=20)
    class Meta:
        model = myUser
        fields = ('username', 'name', 'email', 'password1','password2','rule','status')

