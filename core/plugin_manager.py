from django import forms
from muddle.plugins.plugin import Plugin
from muddle.plugins.plugin_manager import PluginManager

from models import TouchscreenPlugin


class GeneralSettingsForm(forms.Form):
    MAX_OPTIMAL_WIDTH = forms.IntegerField(
        label='Maximum Optimal Width',
        help_text='Maximum width optimal for reading',
        initial=780
    )

    DISPLAY_DURATION = forms.IntegerField(
        label='Default Screen Duration',
        help_text='How long screens will be displayed',
        initial=10000
    )

    TIMEOUT = forms.IntegerField(
        label='Default Screen Timeout',
        help_text='Duration of time without activity before the slide show restarts',
        initial=10000
    )
        
    MSG_SEND_URL = forms.CharField(
        label='Message Send URL', 
        help_text='The send url of the message server', 
        initial='http://localhost:9000/?c=1&q=touchscreen',
        max_length=128
    )

    MSG_RECEIVE_URL = forms.CharField(
        label='Message Receive URL', 
        help_text='The receive url of the message server', 
        initial='http://localhost:9000/?c=0&q=touchscreen',
        max_length=128
    )

class ScreenManager(TouchscreenPlugin, PluginManager):
    """
    Manager that registers screens
    """
    description = 'Manager that registers screens'
    config_form = GeneralSettingsForm
    
    def update_config(self, config):
        """
        Overridden to store copy of config within this class.  By default it
        just unpacks all values to this plugin
        """
        super(TouchscreenPlugin, self).update_config(config)
        self.config = config
    
    def __init__(self, *args, **kwargs):
        TouchscreenPlugin.__init__(self, *args, **kwargs)
        PluginManager.__init__(self)
    
    def get_settings(self):
        """
        Aggregates settings from all the plugins
        """
        touchscreen_settings = {'general':self.config.config}
        return touchscreen_settings

