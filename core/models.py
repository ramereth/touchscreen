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
    hash        = models.CharField(unique=True, max_length=255)
    enabled     = models.BooleanField(default=True)
    name        = None
    description = None

    class Meta:
        abstract = True

    def generate_hash(self):
        return 'asdfasdf%s' % self.name

    def validate(self):
        if not name:
            raise 'Plugin name cannot be null'

        if not description:
            raise 'Plugin description cannot be null'

        return True


class Screen(Plugin):
    duration    = models.IntegerField(default=None, null=True)
    template    = None
    css         = None
    javascript  = None

    def validate(self):
        super.validate(self)

        if not template:
            raise 'Plugin template cannot be null'

        return True

    def __init__(self, template, name, *args, **kwargs):
        Plugin.__init__(self, *args, **kwargs)
        self.name = name
        self.template = template
        self.hash = self.generate_hash()
