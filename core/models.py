from django import forms
from muddle.plugins.plugin import Plugin


class TouchscreenPlugin(Plugin):
    pass


class ScreenGeneralSettings(forms.Form):
    duration    = forms.IntegerField(initial=10000, required=False)
    slideshow   = forms.BooleanField(initial=True)


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

class ScreenAnimation(TouchscreenPlugin):
    """
    Plugin for screen hide/show animations.
    """
    target = 'ScreenAnimationManager'
    _target = 'ScreenAnimationManager'
    template = None
    
    def __init__(self, *args, **kwargs):
        super(ScreenAnimation, self).__init__(*args, **kwargs)
        self.hash = self.name().lower()