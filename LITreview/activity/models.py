from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db import models


class Ticket(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    image = models.FileField(upload_to="tickets/")
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="tickets")
    time_created = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE, related_name="reviews")
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    headline = models.CharField(max_length=128)
    body = models.CharField(max_length=8192, blank=True)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    time_created = models.DateTimeField(auto_now_add=True)

class UserFollows(models.Model):
    follower = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='followed_users')
    followed = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='followers')
    class Meta:
        # ensures we don't get multiple UserFollows instances
        # for unique user-user_followed pairs
        unique_together = ('follower', 'followed', )
