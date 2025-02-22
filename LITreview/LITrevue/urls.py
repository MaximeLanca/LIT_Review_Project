
from django.contrib import admin
from django.urls import path
from activity import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('new-ticket/', views.create_ticket, name='create_ticket'),
    path('new-review/', views.create_review, name='create_review'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)