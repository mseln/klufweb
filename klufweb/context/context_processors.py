import os
from feed.models import NewsArticle

def articles(request):
    articles = NewsArticle.objects.all().order_by('-created')[0:4]
    c = {'articles': articles}
    return c
