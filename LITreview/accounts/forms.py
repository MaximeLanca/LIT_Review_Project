from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CustomUserCreationForm(UserCreationForm):
    email= forms.EmailField(required=True, label="Adresse Email")

    class Meta(UserCreationForm.Meta):
        model = User
        fields=("username","email","password1","password2")

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label='Non d"utilisateur')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')