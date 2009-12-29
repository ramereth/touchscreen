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

screen_people_settings = screen_peopleSettings('screen_people Settings')

