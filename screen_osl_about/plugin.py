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

screen_osl_about = Screen( 
    # Required Parameters --------------------------------------
    'screen_osl_about.html', # the screen's file name
    'screen_osl_about',      # the screen's name

    # Optional Parameters --------------------------------------
    duration=300000, # how long to display the screen
    hide='slide',    # the hide transition
    show='slide',    # the show transition
    slideshow=True,  # include the screen in the slideshow?

    js_init ='screen_osl_about_init',  # a function to call when
                                       # initializing the screen

    js_start='screen_osl_about_start', # a function to call when
                                       # showing the screen

    js_stop ='screen_osl_about_stop',  # a function to call when
                                       # hiding the screen
)


