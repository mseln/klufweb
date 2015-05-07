from django.http import Http404
from django.shortcuts import render
from django.views.generic import View
from django.template import RequestContext

from feed.models import NewsArticle
from feed.models import Event

from feed.templatetags import ext_img
from django import template
register = template.Library()

class News(View):

    news_per_page = 5 
    template_name = 'feed/news.html'

    def get(self, request, *args, **kwargs):
        reqcon = RequestContext(request)

        if(len(kwargs) == 0): # no argument for page
            curr_page = 0
            articles = NewsArticle.objects.all().order_by('-created')[0:self.news_per_page]
        elif(len(kwargs) == 1): # argument for page exists
            curr_page = int(kwargs['page'])
            first = 0 + self.news_per_page * curr_page
            last  = self.news_per_page + self.news_per_page * curr_page 
            articles = NewsArticle.objects.all().order_by('-created')[first:last]

        prev_deactivated = curr_page <= 0
        next_deactivated = (curr_page + 1)*self.news_per_page >= NewsArticle.objects.all().count()

        page = {'curr': curr_page, 'next': curr_page+1, 'prev': curr_page-1,
                'prev_deactivated': prev_deactivated, 'next_deactivated': next_deactivated}

        context = {'reqcon': reqcon, 'articles': articles, 'page': page}

        return render(request, self.template_name, context)


class NewsPage(View):
    template_name = 'feed/news_page.html'

    def get(self, request, q_id, slug, *args, **kwargs):
        reqcon = RequestContext(request)

        try:
            article = NewsArticle.objects.get(id=q_id)
            if article.slug != slug:
                raise NameError('Slug does not match id')
        except:
            raise Http404

        context = {'reqcon': reqcon, 'article': article}
        return render(request, self.template_name, context)


class Schedule(View):
    def get(self, request, *args, **kwargs):

        reqcon = RequestContext(request) 
        events = Event.objects.all().order_by('-created') 
        context = {'reqcon': reqcon, 'events': events}
        
        return render(request, "feed/schedule.html", context)
