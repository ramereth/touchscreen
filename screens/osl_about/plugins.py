from core.models import *

"""
create instance of screens this plugin provides. The parameters are as follows:

	Required:
	- the name of the screen's html file (i.e. 'screen.html')
	- the name of the screen (i.e. 'screen')

	Optional:
	- hide='<transition name>'	i.e. hide='fade', or hide='slide'
	- show='<transition name>'	i.e. show='fade', or show='slide'
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

class AboutGeneralSettingsForm(ScreenGeneralSettings):
    DISPLAY_DURATION = forms.IntegerField(
        label='Default Screen Duration',
        help_text='How long screens will be displayed',
        initial=300000
    )

class OSL_About(Screen):
    description = 'Screen displaying generation information about the open source lab'
    template = 'osl_about.html' # the screen's file name
    js_init ='init'  # a function to call when initializing the screen
    js_start='start' # a function to call when showing the screen
    js_stop ='stop'  # a function to call when hiding the screen
    js_onWinResize = 'onWinResize' # a function to call when window gets resized

