from django.core import validators
from django import forms
from .models import Data
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation


class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput(attrs={'class': 'input',
                                                                  'type': 'password', 'placeholder': 'Enter Password'}))
    password2 = forms.CharField(label='Confirm Password',
                                widget=forms.PasswordInput(attrs={'class': 'input', 'type': 'password',
                                                                  'placeholder': 'Enter Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        labels = {'email': 'Email'}
        widgets = {'username': forms.TextInput(attrs={'class': 'input', 'type': 'text', 'placeholder': 'Enter UserName'})}


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'input',
                                                           'placeholder': 'Enter UserName'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'input', 'id': 'myInput',
               'placeholder': 'Enter Your Password'}))


class UserDataInsert(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['Sample_received', 'Sequence_last', 'Sample_pending', 'Sample_rejected', 'Reason', 'Remark']
        widgets = {
            'Sample_received': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter Sample Received',
                                                      'id': 'sample_received'}),
            'Sequence_last': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter Sequence Last Week',
                                                    'id': 'sequence'}),
            'Sample_pending': forms.TextInput(attrs={'class': 'input', 'readonly': 'readonly', 'id': 'pending'}),
            'Sample_rejected': forms.TextInput(attrs={'class': 'input'}),
            'Reason': forms.TextInput(attrs={'class': 'input'}),
            'Remark': forms.TextInput(attrs={'class': 'input'}),
        }
