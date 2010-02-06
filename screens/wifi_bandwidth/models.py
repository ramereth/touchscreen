from django.db import models
import dbsettings

""" ================================================================
# Settings for screen_webcams
================================================================ """
class wifi_bandwidthSettings( dbsettings.Group ):
    
    img_addr = dbsettings.StringValue(
            'Campus WiFi bandwidth map URL', 
            'URL of the WiFi bandwidth map', 
            default='http://oregonstate.edu/net/wifi_map/wifi_bandwidth_map.png'
    )
    
    imgRefreshInterval = dbsettings.IntegerValue(
            'Image Refresh Interval', 
            'The time interval to refresh the images, in milliseconds', 
            default=30000
    )

wifi_bandwidth_settings = wifi_bandwidthSettings('wifi_bandwidth Settings')

