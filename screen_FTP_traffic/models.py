from django.db import models
import dbsettings

""" ================================================================
# Settings for screen_FTP_traffic
================================================================ """
class screen_FTP_trafficSettings( dbsettings.Group ):
    
    img_addr = dbsettings.StringValue(
            'FTP traffic map URL', 
            'URL of the FTP traffic map', 
            default='http://larch.osuosl.org/ftpmap/weathermap.png'
    )
    
    imgRefreshInterval = dbsettings.IntegerValue(
            'Image Refresh Interval', 
            'The time interval to refresh the image, in milliseconds', 
            default=30000
    )

screen_FTP_traffic_settings = screen_FTP_trafficSettings('screen_FTP_traffic Settings')

