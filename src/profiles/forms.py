from django import forms
from django.contrib.auth.forms import UserCreationForm


from .models import Profile


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ('username', 'user', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'user': forms.TextInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
        }