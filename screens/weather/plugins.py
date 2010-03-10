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

class WeatherSettings(forms.Form):
    # Original Weather.com URL:
    # http://xoap.weather.com/weather/local/USOR0076?cc=*&dayf=5&prod=xoap&par=1003666583&key=4128909340a9b2fc
    
    weather_feed_URL = forms.CharField(
        label='Weather.com Feed URL',
        help_text='URL of the weather.com weather feed',
        initial='http://xoap.weather.com/weather/local/USOR0076?cc=*&dayf=5&prod=xoap',
        max_length=128
    )

    weather_feed_main_key_URL = forms.CharField(
        label='Weather.com Feed Main Key',
        help_text='Main key for the weather.com feed',
        initial='4128909340a9b2fc',
        max_length=128
    )

    weather_feed_par_key_URL = forms.CharField(
        label='Weather.com Feed Partner Key',
        help_text='Partner key for the weather.com feed',
        initial='1003666583',
        max_length=128
    )

    forecast_icon_height = forms.IntegerField(
        label='Forecast Icon Height',
        help_text='Height of the forecast icons.',
        initial=50
    )

    refresh_interval = forms.IntegerField(
        label='Refresh Interval',
        help_text='How often to refresh the data (in milliseconds.)',
        initial=600000
    )

    maps_cycle_timeout = forms.IntegerField(
        label='Maps Cycle Timeout',
        help_text='How long each map is displayed (in milliseconds.)',
        initial=5000
    )


class Weather(Screen):
    template='weather.html'
    description='Weather powered by weather.com'

    #optional params
    config_form = (WeatherSettings, ScreenGeneralSettings)
    js_init ='init'
    js_start='start'
    js_stop ='stop'
    js_onWinResize = 'onScreenResize'