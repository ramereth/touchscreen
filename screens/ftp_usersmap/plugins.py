from core.models import Screen, ScreenGeneralSettings
from django import forms


class FTP_Users_Map(Screen):    
    template='ftpusersmap.html'
    description='Realtime sample of ftp users'

    #optional params
    config_form=(ScreenGeneralSettings)
    show='fade'
    hide='fade'
    js_init ='init'
    js_start='start'
    js_stop ='stop'
    js_onWinResize = 'onWinResize'