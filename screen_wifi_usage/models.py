from django.db import models
import dbsettings

""" ================================================================
# Settings for screen_webcams
================================================================ """
class screen_wifi_usageSettings( dbsettings.Group ):
    
    img_addr = dbsettings.StringValue(
            'Campus WiFi usage map URL', 
            'URL of the WiFi usage map', 
            default='http://oregonstate.edu/net/wifi_map/wifi_usage_map.png'
    )

screen_wifi_usage_settings = screen_wifi_usageSettings('screen_wifi_usage Settings')
