
from django.contrib import admin
from django.urls import path
from activity.views import create_ticket, create_review, home, display_feed_tickets, display_followers
from django.conf.urls.static import static
from django.conf import settings
from accounts.views import signUp, LoginPage, logout_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',LoginPage.as_view(), name="login"),
    path('home/', home, name='home'),
    path('new-ticket/', create_ticket, name='create_ticket'),
    path('new-review/', create_review, name='create_review'),
    path('registration/',signUp, name="signUp"), 
    path('logout/', logout_user, name='logout'),
    path('feed/', display_feed_tickets, name='feed'),
    path('followers/', display_followers, name='followers'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)