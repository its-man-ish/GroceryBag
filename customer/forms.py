from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import *

from django import forms

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('email','username','password1','password2')


class UserUpdateForm(UserChangeForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('email','username','first_name','last_name')


class ProfileModelForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('first_name','last_name','gender','country','avatar')
     
