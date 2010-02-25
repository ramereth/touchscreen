from django import forms
from muddle.plugins.plugin import Plugin

'''
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
'''
class TouchscreenPlugin(Plugin):
    pass


class ScreenGeneralSettings(forms.Form):
    duration    = forms.IntegerField(initial=10000, required=False)
    hide        = forms.CharField(max_length='30', initial="slide")
    show        = forms.CharField(max_length='30', initial="slide")
    slideshow   = forms.IntegerField(initial=1)


class Screen(TouchscreenPlugin):
    """
    Plugin for screens.  A screen is a single view that can be shown
    on the display.
    """
    target = 'ScreenManager'
    _target = 'ScreenManager'

    config_form = ScreenGeneralSettings

    # fields that are not parameters so they do not need to be changed on the fly
    template    = None      # template for the screen
    js_init = None          # javascript initialization function called on screen load
    js_start = None         # javascript start function called on screen show
    js_stop = None          # javascript stop function called on screen hide
    js_onWinResize = None   # javascript function called when window is resized
    hide='slide'            # hide animation
    show='slide'            # show animation
    slideshow=True          # include in slideshow

    

    def __init__(self, *args, **kwargs):
        super(Screen, self).__init__(*args, **kwargs)
        
        self.hash = self.name()
        
        # add general settings for all screens combine with user defined
        '''# settings which might be a list, tuple, or single class
        if self.config_form:
            if isinstance(self.config_form, (list,)):
                self.config_form.append(ScreenGeneralSettings)
            elif isinstance(self.config_form, (tuple,)):
                self.config_form = self.config_form + (ScreenGeneralSettings,)
            else:
                self.config_form = (ScreenGeneralSettings, self.config_form)
        else:
            self.config_form = ScreenGeneralSettings
        '''

