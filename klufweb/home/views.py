from django.shortcuts import render
from django.views.generic import View
from django.template import RequestContext

class Home(View):
    template_name = 'home/home.html'

    def get(self, request, *args, **kwargs):
        reqcon = RequestContext(request)
        context = {'reqcon': reqcon}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        pass

