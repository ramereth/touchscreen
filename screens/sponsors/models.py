from django.db import models
import dbsettings

""" ================================================================
# Settings for sponsors
================================================================ """
class sponsorsSettings( dbsettings.Group ):
    
    sponsors_URL = dbsettings.StringValue(
        'OSL Sponsors RSS Feed URL', 
        'URL of the RSS feed of the OSL sponsors.', 
        default='http://osuosl.org/members/rss.xml'
    )
    
    friends_URL = dbsettings.StringValue(
        'OSL Friends Page URL', 
        'URL of the page listing the friends of the OSL.', 
        default='http://osuosl.org/friends/members'
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
        'Time between scrolling of a friend (in milliseconds). Must be at least 50 greater than scroll speed.',
        default=3000)
    
    friends_scroll_speed = dbsettings.IntegerValue(
        'Friends Scroll Speed',
        'Time it takes to scroll a single item (in milliseconds). Must be at least 50 less than scroll interval.',
        default=1000)
        
    sponsors_scroll_interval = dbsettings.IntegerValue(
        'Sponsors Scroll Interval',
        'Time between scrolling of a sponsor (in milliseconds). Must be at least 50 greater than scroll speed.',
        default=10000)
        
    sponsors_scroll_speed = dbsettings.IntegerValue(
        'Sponsors Scroll Speed',
        'Time it takes to scroll a single item (in milliseconds). Must be at least 50 less than scroll interval.',
        default=2000)

sponsors_settings = sponsorsSettings('sponsors Settings')
