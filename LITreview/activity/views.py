from django.shortcuts import render, redirect
from .forms import TicketForm, ReviewForm
from .models import Ticket
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db import models


def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            form.user = get_user_model().objects.first() #request.user 
            form.save()
            return redirect('create_ticket')
        print(form.errors)
    else:
        form= TicketForm()
    context = {'form': form}
    return render (request, 'new_ticket.html', context)


def create_review(request):
    if request.method =='POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.user = request.user
            form.save()
            return redirect('create_review')
    else:
        form = ReviewForm()
    context = {'form': form}
    return render (request, 'new_review.html', context)

@login_required
def home(request):
    #flux = models.objects.filter(contributors__in=request.Ticket.all())
    #context = {'flux' : flux,}
    return render (request, 'home.html')

def display_feed_tickets(request):
    tickets = Ticket.objects.all()
    context = {"tickets": tickets}
    return render(request,'feed.html',context)

@login_required
def display_followers(request):
    followed_users = request.user
    context = {"followed_users":followed_users}
    return render(request,'followers.html',context )
