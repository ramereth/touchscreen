from django.db import models
import dbsettings

""" ================================================================
# Settings for screen_weather
================================================================ """
class screen_weatherSettings( dbsettings.Group ):
    
    feed_URL = dbsettings.StringValue(
        'Weather Feed URL', 
        'URL of the weather feed', 
        default='http://www.google.com'
    )

    refresh_interval = dbsettings.IntegerValue(
        'Refresh Interval', 
        'How often to refresh the data (in milliseconds.)', 
        default=60000
    )
    
screen_weather_settings = screen_weatherSettings('screen_weather Settings')

