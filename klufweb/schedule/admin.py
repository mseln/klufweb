from django.contrib import admin
from schedule.models import Event, EventAdmin

admin.site.register(Event, EventAdmin)
