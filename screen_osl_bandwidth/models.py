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
    #  tile size settings
    # =====================

    thumbnail_img_height = dbsettings.IntegerValue(
            'Thumbnail Image Height', 
            'The height of the thumbnail images', 
            default=82
    )
    
    thumbnail_img_width = dbsettings.IntegerValue(
            'Thumbnail Image Width', 
            'The width of the thumbnail images', 
            default=200
    )
    
    mainTile_height = dbsettings.IntegerValue(
            'Main Tile Image Height', 
            'The height of the main tile\'s images', 
            default=202
    )
    
    mainTile_width = dbsettings.IntegerValue(
            'Main Tile Image Width', 
            'The width of the main tile\'s images', 
            default=495
    )

    # ===========================
    #  image address and titles
    # ===========================    
    title_0 = dbsettings.StringValue(
            'Tile 0\'s Title', 
            'The title of the 0th tile', 
            default='Apache'
    )
    
    imgAddr_0a = dbsettings.StringValue(
            'Tile 0\'s 1st Image Address', 
            'Source image address of the 0th tile\'s 1st image', 
            default='http://netfoo.nero.net/netviewer/img/OSUOSL-Apache-Normal-day-ifInOctets-100000000000-AVERAGE.png'
    )
    
    imgAddr_0b = dbsettings.StringValue(
            'Tile 0\'s 2nd Image Address', 
            'Source image address of the 0th tile\'s 2nd image', 
            default='http://netfoo.nero.net/netviewer/img/OSUOSL-Apache-Normal-week-ifInOctets-100000000000-AVERAGE.png'
    )
    
    title_1 = dbsettings.StringValue(
            'Tile 1\'s Title', 
            'The title of the 1st tile', 
            default='Gentoo'
    )
    
    imgAddr_1a = dbsettings.StringValue(
            'Tile 1\'s 1st Image Address', 
            'Source image address of the 1st tile\'s 1st image', 
            default='http://netfoo.nero.net/netviewer/img/OSUOSL-Gentoo-Normal-day-ifInOctets-100000000000-AVERAGE.png'
    )
    
    imgAddr_1b = dbsettings.StringValue(
            'Tile 1\'s 2nd Image Address', 
            'Source image address of the 1st tile\'s 2nd image', 
            default='http://netfoo.nero.net/netviewer/img/OSUOSL-Gentoo-Normal-week-ifInOctets-100000000000-AVERAGE.png'
    )
    
    title_2 = dbsettings.StringValue(
            'Tile 2\'s Title', 
            'The title of the 2nd tile', 
            default='Kernel.org'
    )
    
    imgAddr_2a = dbsettings.StringValue(
            'Tile 2\'s 1st Image Address', 
            'Source image address of the 2nd tile\'s 1st image', 
            default='http://netfoo.nero.net/netviewer/img/OSUOSL-Kernel-Normal-day-ifInOctets-100000000000-AVERAGE.png'
    )
    
    imgAddr_2b = dbsettings.StringValue(
            'Tile 2\'s 2nd Image Address', 
            'Source image address of the 2nd tile\'s 2nd image', 
            default='http://netfoo.nero.net/netviewer/img/OSUOSL-Kernel-Normal-week-ifInOctets-100000000000-AVERAGE.png'
    )
    
    title_3 = dbsettings.StringValue(
            'Tile 3\'s Title', 
            'The title of the 3rd tile', 
            default='OpenOffice.org'
    )
    
    imgAddr_3a = dbsettings.StringValue(
            'Tile 3\'s 1st Image Address', 
            'Source image address of the 3rd tile\'s 1st image', 
            default='http://netfoo.nero.net/netviewer/img/OSUOSL-OpenOffice-Normal-day-ifInOctets-100000000000-AVERAGE.png'
    )
    
    imgAddr_3b = dbsettings.StringValue(
            'Tile 3\'s 2nd Image Address', 
            'Source image address of the 3rd tile\'s 2nd image', 
            default='http://netfoo.nero.net/netviewer/img/OSUOSL-OpenOffice-Normal-week-ifInOctets-100000000000-AVERAGE.png'
    )
    
    title_4 = dbsettings.StringValue(
            'Tile 4\'s Title', 
            'The title of the 4th tile', 
            default='Mozilla'
    )
    
    imgAddr_4a = dbsettings.StringValue(
            'Tile 4\'s 1st Image Address', 
            'Source image address of the 4th tile\'s 1st image', 
            default='http://netfoo.nero.net/netviewer/img/OSUOSL-Mozilla-Normal-day-ifInOctets-100000000000-AVERAGE.png'
    )
    
    imgAddr_4b = dbsettings.StringValue(
            'Tile 4\'s 2nd Image Address', 
            'Source image address of the 4th tile\'s 2nd image', 
            default='http://netfoo.nero.net/netviewer/img/OSUOSL-Mozilla-Normal-week-ifInOctets-100000000000-AVERAGE.png'
    )
    
    title_5 = dbsettings.StringValue(
            'Tile 5\'s Title', 
            'The title of the 5th tile', 
            default='OSL Services'
    )
    
    imgAddr_5a = dbsettings.StringValue(
            'Tile 5\'s 1st Image Address', 
            'Source image address of the 5th tile\'s 1st image', 
            default='http://netfoo.nero.net/netviewer/img/OSUOSL-Services-Normal-day-ifInOctets-100000000000-AVERAGE.png'
    )
    
    imgAddr_5b = dbsettings.StringValue(
            'Tile 5\'s 2nd Image Address', 
            'Source image address of the 5th tile\'s 2nd image', 
            default='http://netfoo.nero.net/netviewer/img/OSUOSL-Services-Normal-week-ifInOctets-100000000000-AVERAGE.png'
    )

screen_osl_bandwidth_settings = screen_osl_bandwidthSettings('screen_osl_bandwidth Settings')
