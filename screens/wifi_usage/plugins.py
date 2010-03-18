from core.models import Screen, ScreenGeneralSettings
from django import forms


class WifiUsageSettings(forms.Form):
    img_addr = forms.CharField(
            label='Campus WiFi usage map URL',
            help_text='URL of the WiFi usage map',
            initial='http://oregonstate.edu/net/wifi_map/wifi_usage_map.png',
            max_length=128
    )
    
    imgRefreshInterval = forms.IntegerField(
            label='Image Refresh Interval',
            help_text='The time interval to refresh the images, in milliseconds',
            initial=30000
    )

class WifiUsage(Screen):
    template='wifi_usage.html'
    description='Map of wifi usage at OSU'

    #optional params
    config_form=(WifiUsageSettings, ScreenGeneralSettings)
    hide="fade"
    show="fade"