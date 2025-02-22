from django.contrib import admin
from activity.models import Ticket

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    pass
