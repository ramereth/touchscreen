from core.models import *
from models import webcams_settings

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

webcams = Screen(
    'webcams.html',
    'webcams',

    #optional params
    duration=300000,
    settings=webcams_settings,
    #hide='fade', 
    #show='fade',
    #slideshow=True,
    js_init ='webcams.init',
    js_start='webcams.start',
    js_stop ='webcams.stop',
    js_onWinResize = 'webcams.onWinResize'
)

