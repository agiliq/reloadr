from django.conf.urls.defaults import *

from django.conf import settings

from polls.models import Poll

urlpatterns = patterns('',
   url(r'^$', 'django.views.generic.list_detail.object_list', { 'queryset': Poll.objects.all() })
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
