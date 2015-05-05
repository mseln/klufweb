from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
admin.autodiscover()

from feed.views import News, NewsPage
from schedule.views import Schedule
from static_page.views import StaticPageHandler

urlpatterns = patterns('',
    (r'^ckeditor/', include('ckeditor.urls')),

    (r'^admin/', include(admin.site.urls)), 

    (r'^$', StaticPageHandler.as_view()), 
    
    (r'^traning$', Schedule.as_view()), 
    (r'^news/$', News.as_view()), 
    (r'^news/p/(?P<page>\d+)/$', News.as_view()), 
    (r'^news/(?P<q_id>\d+)/(?P<slug>[a-z0-9-]+)/$', NewsPage.as_view()), 

    # wildcards
    (r'^s/(?P<static_q>[a-z0-9-]+)$', StaticPageHandler.as_view()), 

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns += staticfiles_urlpatterns()
