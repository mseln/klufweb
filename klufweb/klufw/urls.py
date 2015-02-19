from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
admin.autodiscover()

from home.views import Home
from feed.views import News, NewsPage
from about.views import About

urlpatterns = patterns('',
    (r'^ckeditor/', include('ckeditor.urls')),

    (r'^$', Home.as_view()), 
    (r'^about/$', About.as_view()), 
    (r'^news/$', News.as_view()), 
    (r'^news/p/(?P<page>\d+)/$', News.as_view()), 
    (r'^news/(?P<q_id>\d+)/(?P<slug>[a-z0-9-]+)/$', NewsPage.as_view()), 

    (r'^admin/', include(admin.site.urls)), 
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns += staticfiles_urlpatterns()
