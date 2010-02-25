from django import forms

from core.models import *

"""
create instance of screens this plugin provides. The parameters are as follows:

	Required:
	- the name of the screen's html file (i.e. 'screen.html')
	- the name of the screen (i.e. 'foo_screen')

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

class FTP_Traffic(Screen):
    description = 'Map of bandwidth usage by the OSL and its mirrors'
    template = 'ftp_traffic.html'
    config_form = (FTPTrafficSettings, ScreenGeneralSettings)
    js_init ='init'
    js_start='start'
    js_stop ='stop'
    js_onWinResize = 'onScreenResize'
