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
    RATING_CHOICES = [(i, str(i)) for i in range(6)]
    rating = forms.ChoiceField(
        choices=RATING_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'radio-wrapper'}),
        label="Note"
    )
    class Meta:
        model = Review
        exclude = ['user', 'ticket']
        labels = {
                'headline': 'Commentaire',
                'body': 'Votre critique',
            }
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user',None)
        self.ticket = kwargs.pop('ticket', None)
        super().__init__(*args, **kwargs)
        self.fields['rating'].widget.attrs.update({'class': 'radio-wrapper'})

    def save(self,commit=True):
        review=super().save(commit=False)
        review.user = self.user
        review.ticket = self.ticket
        review.save()
        return review

