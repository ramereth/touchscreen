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
	- duration='<time in ms>'	How long screen will be displayed. I.e. 
								duration='3000' means to display the screen for 
								3 seconds.
	- slideshow='<true or false>'	If the screen is to be included in the 
									slideshow
	- js_init='<js function>'	a javascript function to call when the screen is
								initialized.
	- js_start='<js function>'	a javascript function to call when showing the 
								screen
	- js_stop='<js function>'	a javascript function to call when hiding the 
								screen

"""
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
    js_init ='init'
    js_start='start'
    js_stop ='stop'
    js_onWinResize = 'onWinResize'