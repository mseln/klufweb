from django.shortcuts import render
from django.views.generic import View
from django.template import RequestContext

class About(View):
    template_name = 'about/about.html'

    def get(self, request, *args, **kwargs):
        reqcon = RequestContext(request)
        context = {'reqcon': reqcon}
        return render(request, self.template_name, context)

