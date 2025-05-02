from django import forms
from .models import Ticket, Review

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user',None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        ticket=super().save(commit=False)
        if self.user is not None:
            ticket.user = self.user
        if commit:
            ticket.save()
        return ticket

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['ticket', 'rating', 'headline', 'body']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user',None)
        super().__init__(*args, **kwargs)
        
    def save(self,commit=True):
        review=super().save(commit=False)
        review.user = self.user
        review.save()
        return review

