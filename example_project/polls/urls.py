from django.conf.urls.defaults import *

from polls.models import Poll

urlpatterns = patterns('',
   url(r'^$', 'django.views.generic.list_detail.object_list', { 'queryset': Poll.objects.all() })
)
