import requests
from .models import *
from django.shortcuts import render, redirect
from django.views import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime, timedelta

# Create your views here.
class HomePage(View):
    template_name = 'index.html'
    
    def get(self, request):
        return render(request, self.template_name)
    
class MasstimePage(View):
    template_name = 'masstime.html'
    
    def get(self, request):
        return render(request, self.template_name)
    
def video_list(request):
    # Retrieve all instances of VideoModel from the database
    videos = VideoModel.objects.all().order_by('-date')

    # Apply search filter based on duration
    duration = request.GET.get('duration', 'all')
    if duration != 'all':
        start_time = calculate_start_time(duration)
        videos = videos.filter(date__gte=start_time)

    # Pagination
    paginator = Paginator(videos, 10)  # Show 10 videos per page
    page_number = request.GET.get('page')
    try:
        videos_paginated = paginator.page(page_number)
    except PageNotAnInteger:
        videos_paginated = paginator.page(1)
    except EmptyPage:
        videos_paginated = paginator.page(paginator.num_pages)

    return render(request, 'video.html', {'videos': videos_paginated, 'duration': duration})

def calculate_start_time(duration):
    now = datetime.now()
    if duration == '1h':
        return now - timedelta(hours=1)
    elif duration == '1d':
        return now - timedelta(days=1)
    elif duration == '1w':
        return now - timedelta(weeks=1)
    elif duration == '1m':
        return now - timedelta(weeks=4)
    elif duration == '1y':
        return now - timedelta(weeks=52)
    else:
        return None

def event_list(request):
    duration = request.GET.get('duration', 'all')

    if duration == '1h':
        start_time = datetime.now() - timedelta(hours=1)
    elif duration == '1d':
        start_time = datetime.now() - timedelta(days=1)
    elif duration == '1w':
        start_time = datetime.now() - timedelta(weeks=1)
    elif duration == '1m':
        start_time = datetime.now() - timedelta(weeks=4)
    elif duration == '1y':
        start_time = datetime.now() - timedelta(weeks=52)
    else:
        start_time = None

    if start_time:
        events = EventModel.objects.filter(date__gte=start_time).order_by('-date')
    else:
        events = EventModel.objects.all().order_by('-date')

    # Pagination
    paginator = Paginator(events, 10)  # Show 10 events per page
    page = request.GET.get('page')
    try:
        paginated_events = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        paginated_events = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        paginated_events = paginator.page(paginator.num_pages)

    return render(request, 'event.html', {'events': paginated_events, 'duration': duration})

    
class ContactPage(View):
    template_name = 'contact.html'
    
    def get(self, request):
        return render(request, self.template_name)