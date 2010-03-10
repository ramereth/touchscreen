import httplib2
from django.http import HttpResponse

from django.shortcuts import render_to_response
from django.conf import settings
from django.template import RequestContext

from muddle.plugins.managers.root_plugin_manager import RootPluginManager

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


def settings_processor(request):
    return {
        'ROOT':settings.SITE_ROOT,
        'MEDIA':settings.MEDIA_URL
    }


def display(request):
    """ view for displaying display """
    rc = RequestContext(request, processors=[plugin_processor, settings_processor])
    return render_to_response('display.html', {
        'screens':PLUGIN_MANAGER['ScreenManager'].plugins,
        'screen_animations':PLUGIN_MANAGER['ScreenAnimationManager'].plugins,
    }, context_instance=rc)


def menu(request):
    """ View for displaying menu """
    return render_to_response('menu.html')


def proxy(request):
    """ a simple proxy for pulling in external content via ajax """
    connection = httplib2.Http()
    url = request.POST['url']
    response, content = connection.request( url, "GET" )
    return HttpResponse( content )
