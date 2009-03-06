from django.shortcuts import render_to_response
from django.conf import settings
from django.template import RequestContext

from plugin_manager import *

PLUGIN_MANAGER = None

def plugin_processor(request):
    global PLUGIN_MANAGER

    if PLUGIN_MANAGER == None:
        PLUGIN_MANAGER = PluginManager()
        PLUGIN_MANAGER.autodiscover()

    return {'plugin_manager':PLUGIN_MANAGER,
            'settings':PLUGIN_MANAGER.get_settings()
            }

# Create your views here.
def display(request):

    rc = RequestContext(request, processors=[plugin_processor])

    return render_to_response('display.html', {
        'screens':PLUGIN_MANAGER.screens,
    }, context_instance=rc)


def menu(request):
   pass
