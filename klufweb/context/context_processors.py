import os
from feed.models import NewsArticle
from schedule.models import Event

def articles(request):
    articles = NewsArticle.objects.all().order_by('-created')[0:4]
    c = {'articles': articles}
    return c

def events(request):
    events = Event.objects.all().order_by('-event_time')[0:4]
    c = {'events': events}
    return c
