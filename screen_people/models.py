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
    
    auto_rotation_interval = dbsettings.IntegerValue(
        'Auto Rotation Interval',
        'Time between people auto rotations (in milliseconds).',
        default=10000
    )
    
    rotation_pause_timeout = dbsettings.IntegerValue(
        'Auto Rotation Pause Timeout',
        'Time from when a person is explicitly selected to be shown to when auto rotation starts again (in milliseconds).',
        default=180000
    )
    
screen_people_settings = screen_peopleSettings('screen_people Settings')

