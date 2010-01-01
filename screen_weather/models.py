from django.db import models
import dbsettings

""" ================================================================
# Settings for screen_weather
================================================================ """
class screen_weatherSettings( dbsettings.Group ):
    
    feed_URL = dbsettings.StringValue(
        'Weather Feed URL', 
        'URL of the weather feed', 
        default='http://xoap.weather.com/weather/local/USOR0076?cc=*&dayf=5&prod=xoap&par=1003666583&key=4128909340a9b2fc'
    )

    refresh_interval = dbsettings.IntegerValue(
        'Refresh Interval', 
        'How often to refresh the data (in milliseconds.)', 
        default=60000
    )
    
screen_weather_settings = screen_weatherSettings('screen_weather Settings')

