from django.core import validators
from django import forms
from .models import Data
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation


class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        labels = {'email': 'Email'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'})}


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control'}))


class UserDataInsert(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['sample_rec', 'seq_last', 'sample_pen', 'sample_rejected', 'reason', 'remark']
        widgets = {
            'sample_rec': forms.TextInput(attrs={'class': 'form-control'}),
            'seq_last': forms.TextInput(attrs={'class': 'form-control'}),
            'sample_pen': forms.TextInput(attrs={'class': 'form-control'}),
            'sample_rejected': forms.TextInput(attrs={'class': 'form-control'}),
            'reason': forms.TextInput(attrs={'class': 'form-control'}),
            'remark': forms.TextInput(attrs={'class': 'form-control'}),
        }
