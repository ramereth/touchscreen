from django import forms
from core.models import *


class FTPTrafficSettings(forms.Form):
    img_addr = forms.CharField(
            label='FTP traffic map URL',
            help_text='URL of the FTP traffic map',
            initial='http://larch.osuosl.org/ftpmap/weathermap.png',
            max_length=128
    )
    
    imgRefreshInterval = forms.IntegerField(
            label='Image Refresh Interval',
            help_text='The time interval to refresh the image, in milliseconds',
            initial=30000
    )


class screens_ftp_traffic(Screen):
    description = 'Map of bandwidth usage by the OSL and its mirrors'
    template = 'ftp_traffic.html'
    config_form = (FTPTrafficSettings, ScreenGeneralSettings)
    show='fade'
    hide='fade'
