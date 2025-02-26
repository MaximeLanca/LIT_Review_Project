
from django.contrib import admin
from django.urls import path
from activity.views import create_ticket, create_review
from accounts.views import signUp, login_page
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login_page, name="login"),
    path('new-ticket/', create_ticket, name='create_ticket'),
    path('new-review/', create_review, name='create_review'),
    path('registration/',signUp, name="signUp"), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)