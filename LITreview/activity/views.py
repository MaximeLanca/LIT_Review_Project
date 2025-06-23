from django.shortcuts import render, redirect, get_object_or_404
from .forms import TicketForm, ReviewForm
from .models import Ticket, UserFollows, Review
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db import models
from django.contrib import messages

@login_required
def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            form.user = request.user
            #form.user = get_user_model().objects.first() #request.user 
            form.save()
            return redirect('feed')
        print(form.errors)
    else:
        form= TicketForm()
    context = {'form': form}
    return render (request, 'new_ticket.html', context)

@login_required
def create_review(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if hasattr(ticket, 'review'):
        messages.error(request, "Ce ticket a déjà été critiqué.")
        return redirect('feed')
    if request.method == 'POST':
        form = ReviewForm(request.POST, user=request.user, ticket=ticket)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form = ReviewForm(user=request.user, ticket=ticket)
    context = {'form': form, 'ticket': ticket}
    return render(request, 'new_review.html', context)

@login_required
def create_ticket_and_review(request):
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES, user=request.user)
        review_form = ReviewForm(request.POST, user=request.user)
        
        if ticket_form.is_valid() and review_form.is_valid():
         
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            
            return redirect('home')
    else:
        ticket_form = TicketForm()
        review_form = ReviewForm()

    context = {
        'ticket_form': ticket_form,
        'review_form': review_form,
    }
    return render(request, 'new_ticket_and_review.html', context)

@login_required
def home(request):
    #flux = models.objects.filter(contributors__in=request.Ticket.all())
    #context = {'flux' : flux,}
    return render (request, 'home.html')

@login_required
def display_feed(request):
    user = request.user
    followed_users = user.followed_users.values_list('followed_id', flat=True)
    all_connected_users = list(followed_users) + [user.id]

    tickets = Ticket.objects.filter(user_id__in=all_connected_users)
    reviews = Review.objects.filter(user_id__in=all_connected_users)

    feed_items = list(tickets) + list (reviews)
    feed_items.sort(key=lambda item: item.time_created, reverse=True)
    context = {'feed_items': feed_items}
    return render(request,'feed.html',context)
@login_required
def display_user_posts(request):
    user = request.user
    tickets = Ticket.objects.filter(user=user)
    reviews = Review.objects.filter(user=user)

    posts_items = list(tickets) + list (reviews)
    posts_items.sort(key=lambda item: item.time_created, reverse=True)
    context = {'posts_items': posts_items}
    return render(request,'user_posts.html',context)

@login_required
def display_followers(request):
    User = get_user_model()
    followed_users = UserFollows.objects.filter(follower=request.user)
    all_users = User.objects.exclude(id=request.user.id)
    not_followed_users = all_users.exclude(id__in=[user.followed.id for user in followed_users])
    followers = UserFollows.objects.filter(followed=request.user)

    context = {
        "followed_users": followed_users,
        "not_followed_users": not_followed_users,
        "count_followed_users": followed_users.count(),
        "followers": followers,
    }
    return render(request, 'followers.html', context)


@login_required
def follow_user(request, user_id):
    User = get_user_model()
    user_to_follow = get_object_or_404(User, id=user_id)
    if not UserFollows.objects.filter(follower=request.user, followed=user_to_follow).exists():
        UserFollows.objects.create(follower=request.user, followed=user_to_follow)
    return redirect('display_followers')

@login_required
def unfollow_user(request, user_id):
    User = get_user_model()
    user_to_unfollow = get_object_or_404(User, id=user_id)
    UserFollows.objects.filter(follower=request.user, followed=user_to_unfollow).delete()
    return redirect('display_followers')

@login_required
def search_user_to_follow(request):
    User = get_user_model()
    if request.method == "POST":
        username = request.POST.get("username")
        try:
            user_to_follow = User.objects.get(username=username)
            if user_to_follow != request.user and not UserFollows.objects.filter(follower=request.user, followed=user_to_follow).exists():
                UserFollows.objects.create(follower=request.user, followed=user_to_follow)
        except User.DoesNotExist:
            pass
    return redirect('display_followers')

@login_required
def edit_ticket(request, ticket_id):

    ticket = get_object_or_404(Ticket, id=ticket_id, user=request.user)

    if request.user != ticket.user:
        messages.error(request, "Vous n'avez pas l'autorisation de modifier ce ticket.")
        return redirect('feed')
    elif request.method == 'POST':
        form = TicketForm(request.POST, request.FILES, instance=ticket, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form = TicketForm(instance=ticket, user=request.user)

    return render(request, 'edit_ticket.html', {'form': form, 'ticket': ticket})

@login_required
def delete_ticket(request, ticket_id):

    ticket = get_object_or_404(Ticket, id=ticket_id, user=request.user)

    if request.user != ticket.user:
        messages.error(request,"Vous n'avez pas l'autorisation de supprimer ce ticket.")
        return redirect('feed')
    elif request.method == 'POST':
        ticket.delete()
        return redirect('feed')
    return render(request, 'delete_confirm.html', {'object': ticket})


@login_required
def edit_review(request, review_id):

    review = get_object_or_404(Review, id=review_id, user=request.user)

    if request.user != review.user:
        messages.error(request,"Vous n'avez pas l'autorisation de modifier cette critique.")
    elif request.method == 'POST':
        form = ReviewForm(request.POST, instance=review, user=request.user, ticket=review.ticket)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form = ReviewForm(instance=review, user=request.user, ticket=review.ticket)

    return render(request, 'edit_review.html', {'form': form, 'review': review})

@login_required
def delete_review(request, review_id):

    review = get_object_or_404(Review, id=review_id, user=request.user)

    if request.user != review.user:
        messages.error(request,"Vous n'avez pas l'autorisation de supprimer cette critique.")
    elif request.method == 'POST':
        review.delete()
        return redirect('feed')
    return render(request, 'delete_confirm.html', {'object': review})

