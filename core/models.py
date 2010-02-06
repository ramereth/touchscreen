from django.db import models
import dbsettings

""" ================================================================
# General Settings
================================================================ """
class GeneralSettings(dbsettings.Group):

    MAX_OPTIMAL_WIDTH  = dbsettings.IntegerValue(
        'Maximum Optimal Width',
        'Maximum width optimal for reading',
        default=780)

    DISPLAY_DURATION   = dbsettings.IntegerValue(
        'Default Screen Duration',
        'How long screens will be displayed',
        default=10000)

    TIMEOUT            = dbsettings.IntegerValue(
        'Default Screen Timeout',
        'Duration of time without activity before the slide show restarts',
        default=10000)
        
    MENU_URL = dbsettings.StringValue(
        'Menu URL', 
        'URL of the menu application', 
        default='http://localhost:9000/?c=0&q=biggerscreen'
    )

general_settings = GeneralSettings('General Settings')

class Plugin(models.Model):
    """
    Base model for all plugins.
    """
    hash        = models.CharField(unique=True, max_length=255)
    enabled     = models.BooleanField(default=True)
    name        = None
    app         = None
    description = None
    settings    = None

    class Meta:
        abstract = True

    def generate_hash(self):
        # self.hash = '%s_%s' % (self.app, self.name) <-- Original hash
        self.hash = '%s' % self.app.replace('.','_') # sanitize name

        

    def validate(self):
        if not name:
            raise 'Plugin name cannot be null'

        if not description:
            raise 'Plugin description cannot be null'

        return True

class Screen(Plugin):
    """
    Plugin for screens.  A screen is a single view that can be shown
    on the display.
    """
    duration    = models.IntegerField(default=10000, null=True)
    hide        = models.CharField(max_length='30', default="slide")
    show        = models.CharField(max_length='30', default="slide")
    slideshow   = models.IntegerField(default=1)

    # fields that are not parameters so they do not need to be changed on the fly
    template    = None      # template for the screen
    js_init = None          # javascript initialization function called on screen load
    js_start = None         # javascript start function called on screen show
    js_stop = None          # javascript stop function called on screen hide
    js_onWinResize = None   # javascript function called when window is resized

    def validate(self):
        super.validate(self)

        if not template:
            raise 'Plugin template cannot be null'

        return True

    def __init__(self, template, name, duration=10000, settings=None, hide='slide', show='slide', slideshow=True, js_init=None, js_start=None, js_stop=None, js_onWinResize=None, *args, **kwargs):
        Plugin.__init__(self, *args, **kwargs)
        self.name = name
        self.duration = duration
        self.settings = settings
        self.hide = hide
        self.show = show
        self.slideshow = slideshow
        self.template = template
        self.js_init = js_init
        self.js_start = js_start
        self.js_stop = js_stop
        self.js_onWinResize = js_onWinResize
