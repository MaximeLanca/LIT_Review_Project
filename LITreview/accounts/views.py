from django.conf import settings
from django.shortcuts import render ,redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm, LoginForm
from django.views.generic import View
from django.db import models

class LoginPage(View):
    form_class = LoginForm
    template_name = 'authentication.html'

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, {'form': form, 'message': message})
    
    def post(self, request):
        form = self.form_class(request.POST)
        message = ''
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('feed')
            else:
                message = 'Identifiants invalides.'
        return render(request, self.template_name, {'form': form, 'message': message})


def signUp(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration.html', {'form': form})

def login_page(request):
    form = LoginForm()
    message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                message = 'Identifiants invalides.'
    return render(request, 'authentication.html', {'form': form, 'message': message})

def logout_user(request):
    logout(request)
    return redirect('login')
