from django.db import models
from django.contrib import admin
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify

import datetime, time

class BaseArticle(models.Model):
    headline = models.CharField(max_length=200)
    body = RichTextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.timestamp = models.SlugField()
            self.slug = slugify(self.headline)

        super(BaseArticle, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.headline

    class Meta:
        abstract = True

class BaseArticleAdmin(admin.ModelAdmin):
    fields = ('headline', 'body')

    class Meta:
        abstract = True


class NewsArticle(BaseArticle):
    pass

class NewsArticleAdmin(BaseArticleAdmin):
    pass


class Event(BaseArticle):
    location = models.CharField(max_length=50)
    event_time = models.DateTimeField()
    pass

class EventAdmin(BaseArticleAdmin):
    fields = ('headline', 'location', 'event_time', 'body')
    pass
