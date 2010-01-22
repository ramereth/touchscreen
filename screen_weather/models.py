from django.db import models
import dbsettings

""" ================================================================
# Settings for screen_weather
================================================================ """
class screen_weatherSettings( dbsettings.Group ):
    
    # Original Weather.com URL:
    # http://xoap.weather.com/weather/local/USOR0076?cc=*&dayf=5&prod=xoap&par=1003666583&key=4128909340a9b2fc
    
    weather_feed_URL = dbsettings.StringValue(
        'Weather.com Feed URL', 
        'URL of the weather.com weather feed', 
        default='http://xoap.weather.com/weather/local/USOR0076?cc=*&dayf=5&prod=xoap'
    )

    weather_feed_main_key_URL = dbsettings.StringValue(
        'Weather.com Feed Main Key', 
        'Main key for the weather.com feed', 
        default='4128909340a9b2fc'
    )

    weather_feed_par_key_URL = dbsettings.StringValue(
        'Weather.com Feed Partner Key', 
        'Partner key for the weather.com feed', 
        default='1003666583'
    )

    forecast_icon_height = dbsettings.IntegerValue(
        'Forecast Icon Height', 
        'Height of the forecast icons.', 
        default=50
    )

    refresh_interval = dbsettings.IntegerValue(
        'Refresh Interval', 
        'How often to refresh the data (in milliseconds.)', 
        default=60000
    )
    
screen_weather_settings = screen_weatherSettings('screen_weather Settings')

