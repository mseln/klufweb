from django.db import models
from django.contrib import admin
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify

import datetime, time

class BaseEvent(models.Model):
    headline = models.CharField(max_length=200)
    location = models.CharField(max_length=50)
    event_time = models.DateTimeField()

    body = RichTextField(null = True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.timestamp = models.SlugField()
            self.slug = slugify(self.headline)

        super(BaseEvent, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.headline

    class Meta:
        abstract = True

class BaseEventAdmin(admin.ModelAdmin):
    fields = ('headline', 'event_time', 'location', 'body')

    class Meta:
        abstract = True


class Event(BaseEvent):
    pass

class EventAdmin(BaseEventAdmin):
    pass
