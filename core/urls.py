from django.conf.urls.defaults import *

from views import *
from util import get_plugin_static_dirs

urlpatterns = patterns('',
    (r'^$', display),
    (r'^display/$', display),
)


#Load static dirs for any plugins that have a static dir
for app, path in get_plugin_static_dirs():
    urlpatterns += patterns('',
    (r'^static/%s/(?P<path>.*)$' % app, 'django.views.static.serve', {'document_root':  path}),)
