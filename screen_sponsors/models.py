from django.db import models
import dbsettings

""" ================================================================
# Settings for screen_sponsors
================================================================ """
class screen_sponsorsSettings( dbsettings.Group ):
    
    img_addr = dbsettings.StringValue(
            'Campus WiFi usage map URL', 
            'URL of the WiFi usage map', 
            default='http://oregonstate.edu/net/wifi_map/sponsors_map.png'
    )
    
    imgRefreshInterval = dbsettings.IntegerValue(
            'Image Refresh Interval', 
            'The time interval to refresh the images, in milliseconds', 
            default=30000
    )

screen_sponsors_settings = screen_sponsorsSettings('screen_sponsors Settings')

