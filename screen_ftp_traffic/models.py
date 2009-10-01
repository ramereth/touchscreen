from django.db import models
import dbsettings

""" ================================================================
# Settings for screen_ftp_traffic
================================================================ """
class screen_ftp_trafficSettings( dbsettings.Group ):
    
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

screen_ftp_traffic_settings = screen_ftp_trafficSettings('screen_ftp_traffic Settings')

