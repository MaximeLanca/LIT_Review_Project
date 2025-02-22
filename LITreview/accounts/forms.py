from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CustomUserCreationForm(UserCreationForm):
    email= forms.EmailField(required=True, label="Adresse Email")

    class Meta:
        model = User
        field=("username","email","password")

