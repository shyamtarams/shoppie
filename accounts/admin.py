from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin
from .models import myUser
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class CustomUserAdmin(UserAdmin):
    models = myUser
    add_form = CustomUserCreationForm

admin.site.register( myUser, CustomUserAdmin)