from django.shortcuts import render, redirect, get_object_or_404
from .forms import TicketForm, ReviewForm
from .models import Ticket, UserFollows
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
    followed_users = UserFollows.objects.filter(follower=request.user)
    all_users = User.objects.exclude(id=request.user.id)
    not_followed_users = all_users.exclude(id__in=[user.followed.id for user in followed_users])

    context = {
        "followed_users": followed_users,
        "not_followed_users": not_followed_users,
        "count_followed_users": followed_users.count(),
    }
    return render(request, 'followers.html', context)

User = get_user_model()

@login_required
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(User, id=user_id)
    if not UserFollows.objects.filter(follower=request.user, followed=user_to_follow).exists():
        UserFollows.objects.create(follower=request.user, followed=user_to_follow)
    return redirect('display_followers')

@login_required
def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(User, id=user_id)
    UserFollows.objects.filter(follower=request.user, followed=user_to_unfollow).delete()
    return redirect('display_followers')
