from django.contrib import admin
from feed.models import NewsArticle, NewsArticleAdmin

admin.site.register(NewsArticle, NewsArticleAdmin)
