from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2','status')

class SellerSignUpForm(UserCreationForm):
    fullname=forms.CharField(max_length=254)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    status = forms.CharField(max_length=20)
    class Meta:
        model = User
        fields = ('username', 'fullname', 'email', 'password1', 'password2')

