from models import *

class PluginManager():
    
    def __init__(self):
        self.screens={}

    """
    Register a screen with the plugin manager
    """
    def register_screen(self, screen):
        print '[info] PluginManager - Registering Screen: %s' % screen.name
        #make sure the screen is in the db
        try:
            print screen, screen.hash
            Screen.objects.get(hash=screen.hash)
        except:
            #screen wasn't found save it so default values are created
            screen.save()

        # add screen to registry
        self.screens[screen.hash] = screen


    """
    Deregister a screen, stopping it and removing it from the manager
    """
    def deregister_screen(self, key):
        
        # remove the screen from the registry
        del registry[key] 

    def autodiscover(self):
        """
        Auto-discover INSTALLED_APPS tasks.py modules and fail silently when
        not present. This forces an import on them to register any tasks they
        may want.
        """
        import imp
        import inspect
        from django.conf import settings
        print '[info] PluginManager - Autodiscovering Plugins'

        for app in settings.INSTALLED_APPS:
            print '[info] checking app: %s' % app
            # For each app, we need to look for an plugin.py inside that app's
            # package. We can't use os.path here -- recall that modules may be
            # imported different ways (think zip files) -- so we need to get
            # the app's __path__ and look for plugin.py on that path.

            # Step 1: find out the app's __path__ Import errors here will (and
            # should) bubble up, but a missing __path__ (which is legal, but weird)
            # fails silently -- apps that do weird things with __path__ might
            # need to roll their own tasks registration.
            try:
                app_path = __import__(app, {}, {}, [app.split('.')[-1]]).__path__
            except AttributeError:
                continue

            # Step 2: use imp.find_module to find the app's plugin.py. For some
            # reason imp.find_module raises ImportError if the app can't be found
            # but doesn't actually try to import the module. So skip this app if
            # its tasks.py doesn't exist
            try:
                imp.find_module('plugin', app_path)
            except ImportError:
                continue

            # Step 3: load all the plugins in the plugin file
            module = __import__("%s.plugin" % app, {}, {}, ['Screen'])
            #print module
            #print module.__dict__

            for key, plugin in module.__dict__.items():
                if isinstance(plugin, (Screen,)):
                #plugin_instance = object.__new__(plugin)
                    self.register_screen(plugin)

