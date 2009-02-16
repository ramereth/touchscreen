from django.db import models
import dbsettings
from dbsettings.loading import set_setting_value

""" ================================================================
# General Settings
================================================================ """
class GeneralSettings(dbsettings.Group):
    DISPLAY_HEIGHT     = dbsettings.IntegerValue('Screen Height', 'Height of the display screen')
    DISPLAY_WIDTH      = dbsettings.IntegerValue('Screen Width','Width of the display screen')
    MENU_HEIGHT        = dbsettings.IntegerValue('Menu Height', 'Height of the menu screen')
    MENU_WIDTH         = dbsettings.IntegerValue('Menu Width','Width of the menu screen')
    DISPLAY_DURATION   = dbsettings.IntegerValue('Default Screen Duration', 'URL of directory where pdb select files are stored')
    TIMEOUT            = dbsettings.IntegerValue('Screen Timeout', 'Duration of time without activity before the slide show restarts')
general_settings = GeneralSettings('General Settings')

# set defaults for Generic Settings
if not general_settings.DISPLAY_HEIGHT:
    set_setting_value('core.models', '', 'DISPLAY_HEIGHT', 768)
if not general_settings.DISPLAY_WIDTH:
    set_setting_value('core.models', '', 'DISPLAY_WIDTH', 1360)
if not general_settings.MENU_HEIGHT:
    set_setting_value('core.models', '', 'MENU_HEIGHT', 768)
if not general_settings.MENU_HEIGHT:
    set_setting_value('core.models', '', 'MENU_WIDTH', 1024)
if not general_settings.DISPLAY_DURATION:
    set_setting_value('core.models', '', 'DISPLAY_DURATION', 10000)
if not general_settings.TIMEOUT:
    set_setting_value('core.models', '', 'TIMEOUT', 10000)



class Plugin(models.Model):
    """
    Base model for all plugins.
    """
    hash        = models.CharField(unique=True, max_length=255)
    enabled     = models.BooleanField(default=True)
    name        = None
    app         = None
    description = None

    class Meta:
        abstract = True

    def generate_hash(self):
        self.hash = '%s_%s' % (self.app, self.name)

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
    template    = None          # template for the screen
    js_init = None          # javascript initialization function called on screen load
    js_start = None         # javascript start function called on screen show
    js_stop = None          # javascript stop function called on screen hide

    def validate(self):
        super.validate(self)

        if not template:
            raise 'Plugin template cannot be null'

        return True

    def __init__(self, template, name, duration=10000, hide='slide', show='slide', slideshow=1, js_init=None, js_start=None, js_stop=None, *args, **kwargs):
        Plugin.__init__(self, *args, **kwargs)
        self.name = name
        self.duration = duration
        self.hide = hide
        self.show = show
        self.slideshow = slideshow
        self.template = template
        self.js_init = js_init
        self.js_start = js_start
        self.js_stop = js_stop
