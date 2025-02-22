from django.shortcuts import render, redirect
from .forms import TicketForm, ReviewForm
from django.contrib.auth import get_user_model


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
            form.user = get_user_model().objects.first()
            form.save()
            return redirect('create_review')
    else:
        form = ReviewForm()
    context = {'form': form}
    return render (request, 'new_review.html', context)