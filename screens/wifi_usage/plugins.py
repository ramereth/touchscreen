from core.models import Screen, ScreenGeneralSettings
from django import forms

"""
create instance of screens this plugin provides. The parameters are as follows:

	Required:
	- the name of the screen's html file (i.e. 'screen.html')
	- the name of the screen (i.e. 'screen')

	Optional:
	- hide='<transition name>'	i.e. hide='fade', or hide='slide')
	- show='<transition name>'	i.e. show='fade', or show='slide')
	- js_init='<js function>'	a javascript function to call when the screen is
								initialized.
	- js_start='<js function>'	a javascript function to call when showing the 
								screen
	- js_stop='<js function>'	a javascript function to call when hiding the 
								screen

"""

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
    js_init ='init'
    js_start='start'
    js_stop ='stop'
    js_onWinResize = 'onScreenResize'