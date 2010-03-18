from core.models import Screen, ScreenGeneralSettings
from django import forms


class WifiBandwidthSettings(forms.Form):
    img_addr = forms.CharField(
            label='Campus WiFi bandwidth map URL',
            help_text='URL of the WiFi bandwidth map',
            initial='http://oregonstate.edu/net/wifi_map/wifi_bandwidth_map.png',
            max_length=128
    )
    
    imgRefreshInterval = forms.IntegerField(
            label='Image Refresh Interval',
            help_text='The time interval to refresh the images, in milliseconds',
            initial=30000
    )


class WifiBandwidth(Screen):
    template = 'wifi_bandwidth.html'
    description = 'Map of OSU wifi bandwidth usage'

    #optional params
    config_form=(WifiBandwidthSettings, ScreenGeneralSettings)
    show='fade'
    hide='fade'