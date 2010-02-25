import httplib2
from django.http import HttpResponse

from django.shortcuts import render_to_response
from django.conf import settings
from django.template import RequestContext

from muddle.plugins.plugin_manager import RootPluginManager

PLUGIN_MANAGER = None

def plugin_processor(request):
    global PLUGIN_MANAGER

    if PLUGIN_MANAGER == None:
        PLUGIN_MANAGER = RootPluginManager()
        PLUGIN_MANAGER.autodiscover()

    return {
        'plugin_manager':PLUGIN_MANAGER,
        'settings':PLUGIN_MANAGER['ScreenManager'].get_settings()
    }

# The display view
def display(request):
    rc = RequestContext(request, processors=[plugin_processor])
    return render_to_response('display.html', {
        'screens':PLUGIN_MANAGER['ScreenManager'].plugins,
    }, context_instance=rc)

# The menu view
def menu(request):
    return render_to_response('menu.html')

# A simple proxy
def proxy(request):
    connection = httplib2.Http()
    url = request.POST['url']
    response, content = connection.request( url, "GET" )
    return HttpResponse( content )
