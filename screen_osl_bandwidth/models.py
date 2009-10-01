from django.db import models
import dbsettings

""" ================================================================
# Settings for screen_osl_bandwidth
================================================================ """
class screen_osl_bandwidthSettings( dbsettings.Group ):

    # ==================
    #  general settings
    # ==================
    
    imgRefreshInterval = dbsettings.IntegerValue(
            'Image Refresh Interval', 
            'The time interval to refresh the images, in milliseconds', 
            default=30000
    )

    # =====================
    #  image size settings
    # =====================

    thumbnail_height = dbsettings.IntegerValue(
            'Thumbnail Tile Height', 
            'The height of the thumbnail tiles', 
            default=120
    )
    
    thumbnail_width = dbsettings.IntegerValue(
            'Thumbnail Tile Width', 
            'The width of the thumbnail tiles', 
            default=160
    )
    
    mainTile_height = dbsettings.IntegerValue(
            'Main Tile Tile Height', 
            'The height of the main tile\'s tiles', 
            default=480
    )
    
    mainTile_width = dbsettings.IntegerValue(
            'Main Tile Tile Width', 
            'The width of the main tile\'s tiles', 
            default=640
    )

    # ============================
    #  image addresses and titles
    # ============================
    
    imgAddr_0t = dbsettings.StringValue(
            'Tile 0\'s Top Image Address', 
            'Source image address of the 0th tile\'s top image', 
            default='http://netfoo.nero.net/netviewer/img/OSUOSL-Apache-Normal-day-ifInOctets-100000000000-AVERAGE.png'
    )
    
    imgAddr_0b = dbsettings.StringValue(
            'Tile 0\'s Bottom Image Address', 
            'Source image address of the 0th tile\'s bottom image', 
            default='http://netfoo.nero.net/netviewer/img/OSUOSL-Apache-Normal-week-ifInOctets-100000000000-AVERAGE.png'
    )


    title_1 = dbsettings.StringValue(
            'Tile 0\'s Title', 
            'The title of the 0th tile', 
            default='Apache'
    )

screen_osl_bandwidth_settings = screen_osl_bandwidthSettings('screen_osl_bandwidth Settings')
