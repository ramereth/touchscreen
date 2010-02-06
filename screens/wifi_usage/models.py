from django.db import models
import dbsettings

""" ================================================================
# Settings for wifi_usage
================================================================ """
class wifi_usageSettings( dbsettings.Group ):
    
    img_addr = dbsettings.StringValue(
            'Campus WiFi usage map URL', 
            'URL of the WiFi usage map', 
            default='http://oregonstate.edu/net/wifi_map/wifi_usage_map.png'
    )
    
    imgRefreshInterval = dbsettings.IntegerValue(
            'Image Refresh Interval', 
            'The time interval to refresh the images, in milliseconds', 
            default=30000
    )

wifi_usage_settings = wifi_usageSettings('wifi_usage Settings')

