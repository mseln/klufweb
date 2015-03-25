from django.http import Http404
from django.shortcuts import render
from django.views.generic import View
from django.template import RequestContext

from static_page.models import StaticPage

class StaticPage(View):
    template_url = 'static_page/static_page.html'

    def get(self, request, static_q, *args, **kwargs):
        reqcon = RequestContext(request)

        print(StaticPage.objects)

        page = StaticPage.objects.get(slug=static_q)
        try:
            pass
        except:
            raise Http404

        info = "this is static page @ " + static_q + "!\n"
        context = {'reqcon': reqcon, 'info': info}

        return render(request, self.template_url, context)

    def post(self, request, *args, **kwargs):
        pass

