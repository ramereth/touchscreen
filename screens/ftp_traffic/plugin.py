from core.models import *
from models import ftp_traffic_settings

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

ftp_traffic = Screen(
    'ftp_traffic.html',
    'ftp_traffic', 

    #optional params
    duration=300000,
    settings=ftp_traffic_settings,
    #hide='fade', 
    #show='fade',
    slideshow=True,
    js_init ='init',
    js_start='start',
    js_stop ='stop',
    js_onWinResize = 'onScreenResize'
)
