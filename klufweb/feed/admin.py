from django.contrib import admin
from feed.models import NewsArticle, NewsArticleAdmin
from feed.models import Event, EventAdmin

admin.site.register(NewsArticle, NewsArticleAdmin)
admin.site.register(Event, EventAdmin)
