
from django.contrib import admin
from django.urls import path
from activity.views import create_ticket, create_review, home, display_feed, display_followers, follow_user, unfollow_user,search_user_to_follow,create_ticket_and_review,display_user_posts,edit_ticket,delete_ticket,edit_review,delete_review
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
    path('search-follow/', search_user_to_follow, name='search_user_to_follow'),
    path('followers/', display_followers, name='display_followers'),
    path('posts_user/', display_user_posts, name='display_user_posts'),
    path('ticket/<int:ticket_id>/edit/', edit_ticket, name='edit_ticket'),
    path('ticket/<int:ticket_id>/delete/', delete_ticket, name='delete_ticket'),
    path('review/<int:review_id>/edit/', edit_review, name='edit_review'),
    path('review/<int:review_id>/delete/', delete_review, name='delete_review'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)