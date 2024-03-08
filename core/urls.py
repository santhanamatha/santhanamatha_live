from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_view
from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('mass_schedule', MasstimePage.as_view(), name='mass_schedule'),
    path('prayer', PrayerPage.as_view(), name='prayer'),
    path('festival_videos', video_list, name='festival_videos'),
    path('event', event_list, name='event'),
    path('contact', ContactPage.as_view(), name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
