
from django.contrib import admin
from django.urls import path
from activity.views import create_ticket, create_review, home, display_feed, display_followers, follow_user, unfollow_user,search_user_to_follow,create_ticket_and_review
from django.conf.urls.static import static
from django.conf import settings
from accounts.views import signUp, LoginPage, logout_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',LoginPage.as_view(), name="login"),
    path('home/', home, name='home'),
    path('new-ticket/', create_ticket, name='create_ticket'),
    path('new-review/<int:ticket_id>/', create_review, name='create_review'),
    path('new_ticket_and_review/', create_ticket_and_review, name='create_ticket_and_review'),
    path('registration/',signUp, name="signUp"), 
    path('logout/', logout_user, name='logout'),
    path('feed/', display_feed, name='feed'),
    path('follow/<int:user_id>/', follow_user, name='followers'),
    path('unfollow/<int:user_id>/',unfollow_user, name='unfollow_user'),
    path('followers/', display_followers, name='display_followers'),
    path('search-follow/', search_user_to_follow, name='search_user_to_follow'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)