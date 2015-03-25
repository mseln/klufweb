from django.http import Http404
from django.shortcuts import render
from django.views.generic import View
from django.template import RequestContext

from static_page.models import StaticPage

class StaticPageHandler(View):
    template_url = 'static_page/static_page.html'

    def get(self, request, static_q, *args, **kwargs):
        reqcon = RequestContext(request)
        try:
            page = StaticPage.objects.get(slug=static_q)
        except:
            raise Http404
        
        context = {'reqcon': reqcon, 'page': page}

        return render(request, self.template_url, context)

    def post(self, request, *args, **kwargs):
        pass
