from django.http import Http404
from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.template import RequestContext

from static_page.models import StaticPage

class StaticPageHandler(View):
    template_url = 'static_page/static_page.html'
    print("HEJ")

    def get(self, request, static_q=None, *args, **kwargs):
        reqcon = RequestContext(request)
        
        if (static_q == None):
            static_q = "home";
        try:
            page = StaticPage.objects.get(slug=static_q)
        except:
            raise Http404
        
        context = {'reqcon': reqcon, 'page': page}

        return render(request, self.template_url, context)

    def post(self, request, *args, **kwargs):
        pass

def handler404(request):
    response = render_to_response('static_page/404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('static_page/500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response
