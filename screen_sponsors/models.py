from django.db import models
import dbsettings

""" ================================================================
# Settings for screen_sponsors
================================================================ """
class screen_sponsorsSettings( dbsettings.Group ):
    
    sponsors_rss_URL = dbsettings.StringValue(
            'OSL Sponsors RSS Feed URL', 
            'URL of the RSS feed of the OSL sponsors', 
            default='http://osuosl.org/members/rss.xml'
    )
    
    friends_rss_URL = dbsettings.StringValue(
            'OSL Friends Page URL', 
            'URL of the page listing the friends of the OSL', 
            default='http://osuosl.org/friends/members'
    )

screen_sponsors_settings = screen_sponsorsSettings('screen_sponsors Settings')

