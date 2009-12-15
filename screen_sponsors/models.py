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

screen_sponsors_settings = screen_sponsorsSettings('screen_sponsors Settings')

