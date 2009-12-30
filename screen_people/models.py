from django.db import models
import dbsettings

""" ================================================================
# Settings for screen_people
================================================================ """
class screen_peopleSettings( dbsettings.Group ):
    
    people_URL = dbsettings.StringValue(
            'People List URL', 
            'URL of where the people are listed', 
            default='http://osuosl.org/about/people'
    )

    thumbnail_height = dbsettings.IntegerValue(
            'Thumbnail Image Height', 
            'The height of the thumbnail images', 
            default=150
    )
    
    scroll_interval = dbsettings.IntegerValue(
        'Scroll Interval',
        'Time between scrolling (in milliseconds). Must be at least 50 more than scroll speed.',
        default=3000
    )
    
    scroll_speed = dbsettings.IntegerValue(
        'Scroll Speed',
        'Time it takes to scroll a single item (in milliseconds). Must be at least 50 less than scroll interval.',
        default=1000
    )
    
screen_people_settings = screen_peopleSettings('screen_people Settings')

