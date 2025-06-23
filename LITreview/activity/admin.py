from django.contrib import admin
from .models import Ticket
from .models import Review


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'time_created')
    list_filter = ('user',)
    search_fields = ('title', 'description')
    ordering = ('-time_created',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'ticket', 'user', 'rating', 'headline', 'time_created')
    list_filter = ('rating', 'user')
    search_fields = ('headline', 'body')
    ordering = ('-time_created',)


    
