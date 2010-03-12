import httplib2
import simplejson

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.conf import settings
from django.template import RequestContext, Context, loader


from muddle.views import manager
PLUGIN_MANAGER = manager

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
    url = request.GET['url']
    response, content = connection.request( url, "GET" )
    return HttpResponse( content )


def reload(request):
    """ view for reloading a screen """
    screen = PLUGIN_MANAGER['ScreenManager'][request.GET['screen']]
    t = loader.get_template(screen.template)
    context = {'screen':screen}
    context.update(settings_processor(None))
    context.update(plugin_processor(None))
    html = t.render(Context(context))
    screen = {
            'id':screen.hash,
            'hide':screen.hide,
            'show':screen.show,
            'duration': screen.duration,
            'slideshow':int(screen.slideshow),
            'init':screen.js_init,
            'start':screen.js_start,
            'stop':screen.js_stop,
            'onWinResize': screen.js_onWinResize
            }
    
    response = {'screen':screen, 'html':html}
    return HttpResponse(simplejson.dumps(response))