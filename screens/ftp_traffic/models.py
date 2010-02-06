from django.db import models
import dbsettings

""" ================================================================
# Settings for ftp_traffic
================================================================ """
class ftp_trafficSettings( dbsettings.Group ):
    
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

ftp_traffic_settings = ftp_trafficSettings('ftp_traffic Settings')

