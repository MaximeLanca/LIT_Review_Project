from django.shortcuts import render ,redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, LoginForm

def signUp(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration.html', {'form': form})

def login_page(request):
    form = LoginForm()
    massage = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message=f'Bonjour, {user.username}! Vous êtes connecté.'
            else:
                message = 'Identifiants invalides.'
    return render(request, 'authentication.html', {'form': form, 'message': 'message'})

