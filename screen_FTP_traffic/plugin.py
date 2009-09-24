from core.models import *
from models import screen_FTP_traffic_settings

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

screen_FTP_traffic = Screen(
    'screen_FTP_traffic.html',
    'screen_FTP_traffic',

    #optional params
    duration=300000,
    settings=screen_FTP_traffic_settings,
    #hide='fade', 
    #show='fade',
    slideshow=True,
    js_init ='screen_FTP_traffic_init',
    js_start='screen_FTP_traffic_start',
    js_stop ='screen_FTP_traffic_stop',
    js_onWinResize = 'screen_FTP_traffic_onScreenResize'
)

