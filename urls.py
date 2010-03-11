from django.conf.urls.defaults import *
import settings
from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Example:
    # (r'^biggerscreen/', include('biggerscreen.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
    
    #authentication
    (r'^accounts/login/$', login),
    (r'^accounts/logout/$', logout, {'next_page':'/plugins'}),

    # Enable the touchscreen core
    (r'^/*', include('core.urls')),

    # Enable muddle
    (r'^/*', include('muddle.urls')),
    
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':  settings.MEDIA_ROOT}),
)


