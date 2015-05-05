from django.http import Http404
from django.shortcuts import render
from django.views.generic import View
from django.template import RequestContext

from schedule.models import Event

class Schedule(View):
    def get(self, request, *args, **kwargs):

        reqcon = RequestContext(request) 
        events = Event.objects.all().order_by('-created') 
        context = {'reqcon': reqcon, 'events': events}
        
        return render(request, "schedule/schedule.html", context)
