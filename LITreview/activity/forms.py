from django import forms
from .models import Ticket, Review

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']
    def save(self, commit=True):
        ticket=super().save(commit=False)
        ticket.user = self.user
        ticket.save()
        return ticket

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['ticket', 'rating', 'headline', 'body']
    def save(self,commit=True):
        review=super().save(commit=False)
        review.user = self.user
        review.save()
        return review

