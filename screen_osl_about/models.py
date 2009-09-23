from django.db import models
import dbsettings

""" ================================================================
# Settings for screen_osl_about
================================================================ """
class screen_osl_aboutSettings( dbsettings.Group ):
    
    screen_border = dbsettings.IntegerValue(
            'Screen Border', 
            'The space between the edges of the screen and the tiles', 
            default=10
    )
    
    tile_padding = dbsettings.IntegerValue(
            'Tile Padding', 
            'The space between the tiles', 
            default=10
    )

screen_osl_about_settings = screen_osl_aboutSettings('screen_osl_about Settings')
