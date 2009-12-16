from django.db import models
import dbsettings

""" ================================================================
# Settings for screen_sponsors
================================================================ """
class screen_sponsorsSettings( dbsettings.Group ):
    
    sponsors_rss_URL = dbsettings.StringValue(
        'OSL Sponsors RSS Feed URL', 
        'URL of the RSS feed of the OSL sponsors.', 
        default='http://osuosl.org/members/rss.xml'
    )
    
    sponsors_rss_filename = dbsettings.StringValue(
        'OSL Sponsors Downloaded RSS File Name', 
        'File name of the downloaded sponsors RSS XML file.', 
        default='sponsors.xml'
    )
    
    friends_rss_URL = dbsettings.StringValue(
        'OSL Friends Page URL', 
        'URL of the page listing the friends of the OSL.', 
        default='http://osuosl.org/friends/members'
    )

    friends_rss_filename = dbsettings.StringValue(
        'OSL Friends Downloaded RSS XML File Name', 
        'File name of the downloaded friends RSS XML file.', 
        default='sponsors.xml'
    )

    friends_width = dbsettings.IntegerValue(
        'Friends Tile Width',
        'The friends tile width. Will NOT dynamically resize with screen.',
        default=150)
        
    sponsors_max_width = dbsettings.IntegerValue(
        'Sponsors Tile Maximum Width',
        'The sponsors tile maximum width. Will dynamically resize if the width of the sponsors and friends tiles exceeds that of the browser window.',
        default=750)
        
    friends_scroll_interval = dbsettings.IntegerValue(
        'Friends Scroll Interval',
        'Time between scrolling of a friend (in milliseconds)',
        default=3000)
    
    friends_scroll_speed = dbsettings.IntegerValue(
        'Friends Scroll Speed',
        'Time it takes to scroll a single item (in milliseconds)',
        default=1000)
        
    sponsors_scroll_interval = dbsettings.IntegerValue(
        'Sponsors Scroll Interval',
        'Time between scrolling of a sponsor (in milliseconds)',
        default=10000)
        
    sponsors_scroll_speed = dbsettings.IntegerValue(
        'Sponsors Scroll Speed',
        'Time it takes to scroll a single item (in milliseconds)',
        default=2000)

screen_sponsors_settings = screen_sponsorsSettings('screen_sponsors Settings')

