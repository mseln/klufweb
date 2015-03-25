from django.db import models
from django.contrib import admin
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify

import datetime, time

class StaticPage(models.Model):
    slug = models.SlugField()
    page = models.CharField(max_length=200)
    
    body = RichTextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    """
    def save(self, *args, **kwargs):
        if not self.id:
            self.created = models.SlugField()

        self.created = models.SlugField()
        super(StaticPage, self).save(*args, **kwargs)
    """
    

    def __str__(self):
        return self.page

class StaticPageAdmin(admin.ModelAdmin):
    pass
