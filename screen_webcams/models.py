from django.db import models
import dbsettings

""" ================================================================
# Settings for screen_webcams
================================================================ """
class screen_webcamsSettings( dbsettings.Group ):

    # ==================
    #  general settings
    # ==================
    
    screen_border = dbsettings.IntegerValue(
            'Screen Border', 
            'The space between the edges of the screen and the tiles', 
            default=10
    )
    
    imgRefreshInterval = dbsettings.IntegerValue(
            'Image Refresh Interval', 
            'The time interval to refresh the images, in milliseconds', 
            default=30000
    )

    # =====================
    #  image size settings
    # =====================

    thumbnail_height = dbsettings.IntegerValue(
            'Thumbnail Image Height', 
            'The height of the thumbnail images', 
            default=120
    )
    
    thumbnail_width = dbsettings.IntegerValue(
            'Thumbnail Image Width', 
            'The width of the thumbnail images', 
            default=160
    )
    
    mainTile_height = dbsettings.IntegerValue(
            'Main Tile Image Height', 
            'The height of the main tile\'s image', 
            default=480
    )
    
    mainTile_width = dbsettings.IntegerValue(
            'Main Tile Image Width', 
            'The width of the main tile\'s image', 
            default=640
    )

    # =================
    #  image addresses
    # =================
    
    imgAddr_andrews = dbsettings.StringValue(
            'Andrews Forrest image address', 
            'The web address to the current webcam shot', 
            default='http://webcam.oregonstate.edu/live/andrews_current.jpg'
    )

    imgAddr_gill = dbsettings.StringValue(
            'Gill Renovation image address', 
            'The web address to the current webcam shot', 
            default='http://webcam.oregonstate.edu/live/gill_current.jpg'
    )

    imgAddr_south = dbsettings.StringValue(
            'South Campus image address', 
            'The web address to the current webcam shot', 
            default='http://webcam.oregonstate.edu/live/south_current.jpg'
    )
        
    imgAddr_monroe = dbsettings.StringValue(
            'Monroe Street image address', 
            'The web address to the current webcam shot', 
            default='http://webcam.oregonstate.edu/live/monroe_current.jpg'
    )
        
    imgAddr_reser = dbsettings.StringValue(
            'Reser Stadium image address', 
            'The web address to the current webcam shot', 
            default='http://webcam.oregonstate.edu/live/reser1_current.jpg'
    )

    imgAddr_mu = dbsettings.StringValue(
            'Memorial Union image address', 
            'The web address to the current webcam shot', 
            default='http://webcam.oregonstate.edu/live/mu_current.jpg'
    )
        
    imgAddr_library = dbsettings.StringValue(
            'Valley Library image address', 
            'The web address to the current webcam shot', 
            default='http://webcam.oregonstate.edu/live/library_current.jpg'
    )
        
    imgAddr_gloss = dbsettings.StringValue(
            'Gloss Stadium image address', 
            'The web address to the current webcam shot', 
            default='http://webcam.oregonstate.edu/live/baseball_current.jpg'
    )
        
    imgAddr_wave = dbsettings.StringValue(
            'Wave Lab image address', 
            'The web address to the current webcam shot', 
            default='http://webcam.oregonstate.edu/live/wavelab_current.jpg'
    )
        
    imgAddr_hatfield = dbsettings.StringValue(
            'Hatfield Marine Science image address', 
            'The web address to the current webcam shot', 
            default='http://webcam.oregonstate.edu/live/hmsc_current.jpg'
    )
        
    imgAddr_agate = dbsettings.StringValue(
            'Agate Beach image address', 
            'The web address to the current webcam shot', 
            default='http://webcam.oregonstate.edu/live/agate_current.jpg'
    )
        
    imgAddr_wecoma = dbsettings.StringValue(
            'Research Vessel WECOMA image address', 
            'The web address to the current webcam shot', 
            default='http://webcam.oregonstate.edu/live/wecoma_current.jpg'
    )

    # =============
    #  tile titles
    # =============

    title_andrews = dbsettings.StringValue(
            'Andrews Forrest Title', 
            'The title of the Andrews Forest tile', 
            default='Andrews Forrest'
    )
    
    title_gill = dbsettings.StringValue(
            'Gill Renovation Title', 
            'The title of the Gill Renovation tile', 
            default='Gill Renovation'
    )
    
    title_south = dbsettings.StringValue(
            'South Campus Title', 
            'The title of the South Campus tile', 
            default='South Campus'
    )
    
    title_monroe = dbsettings.StringValue(
            'Monroe Street Title', 
            'The title of the Monroe Street tile', 
            default='Monroe Street'
    )
    
    title_reser = dbsettings.StringValue(
            'Reser Stadium Title', 
            'The title of the Reser Stadium tile', 
            default='Reser Stadium'
    )
    
    title_mu = dbsettings.StringValue(
            'Memorial Union Title', 
            'The title of the Memorial Union tile', 
            default='Memorial Union'
    )
    
    title_library = dbsettings.StringValue(
            'Valley Library Title', 
            'The title of the Valley Library tile', 
            default='Valley Library'
    )
    
    title_gloss = dbsettings.StringValue(
            'Gloss Stadium Title', 
            'The title of the Gloss Stadium tile', 
            default='Gloss Stadium'
    )
    
    title_wave = dbsettings.StringValue(
            'Wave Lab Title', 
            'The title of the Wave Lab tile', 
            default='Wave Lab'
    )
    
    title_hatfield = dbsettings.StringValue(
            'Hatfield Marine Science Title', 
            'The title of the Hatfield Marine Science tile', 
            default='Hatfield Marine Science'
    )
    
    title_agate = dbsettings.StringValue(
            'Agate Beach Title', 
            'The title of the Agate Beach tile', 
            default='Agate Beach'
    )
    
    title_wecoma = dbsettings.StringValue(
            'Research Vessel WECOMA Title', 
            'The title of the Research Vessel WECOMA tile', 
            default='Research Vessel WECOMA'
    )

screen_webcams_settings = screen_webcamsSettings('screen_webcams Settings')
