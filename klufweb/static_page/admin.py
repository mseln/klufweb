from django.contrib import admin
from static_page.models import StaticPage, StaticPageAdmin

admin.site.register(StaticPage, StaticPageAdmin)
