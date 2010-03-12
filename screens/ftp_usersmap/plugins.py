from core.models import Screen, ScreenGeneralSettings
from django import forms


class FTPPingMapSettings(forms.Form):
    ping_interval = forms.IntegerField(
            label='Ping Interval',
            help_text='how often to ping the map in milliseconds',
            initial=700,
    )
    
    ping_max = forms.IntegerField(
            label='Ping Max Count',
            help_text='how many pings to leave on the screen before removing them',
            initial=100,
    )


class FTP_Users_Map(Screen):    
    template='ftpusersmap.html'
    description='Realtime sample of ftp users'

    #optional params
    config_form=(FTPPingMapSettings, ScreenGeneralSettings)
    show='fade'
    hide='fade'
    js_init ='init'
    js_start='start'
    js_stop ='stop'
    js_onWinResize = 'onWinResize'