from django.db import models
import dbsettings

""" ================================================================
# Settings for webcams
================================================================ """
class webcamsSettings( dbsettings.Group ):

    # ==================
    #  general settings
    # ==================
    
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

# new models

    # =================
    #  image addresses
    # =================

    imgAddr_0 = dbsettings.StringValue(
            'Webcam 0 image address', 
            'The URL to the current shot for webcam 0', 
            default='http://webcam.oregonstate.edu/live/monroe_current.jpg'
    )

    imgAddr_1 = dbsettings.StringValue(
            'Webcam 1 image address', 
            'The URL to the current shot for webcam 1', 
            default='http://webcam.oregonstate.edu/live/reser1_current.jpg'
    )

    imgAddr_2 = dbsettings.StringValue(
            'Webcam 2 image address', 
            'The URL to the current shot for webcam 2',  
            default='http://webcam.oregonstate.edu/live/mu_current.jpg'
    )

    imgAddr_3 = dbsettings.StringValue(
            'Webcam 3 image address', 
            'The URL to the current shot for webcam 3', 
            default='http://webcam.oregonstate.edu/live/library_current.jpg'
    )

    imgAddr_4 = dbsettings.StringValue(
            'Webcam 4 image address', 
            'The URL to the current shot for webcam 4',  
            default='http://webcam.oregonstate.edu/live/baseball_current.jpg'
    )

    imgAddr_5 = dbsettings.StringValue(
            'Webcam 5 image address', 
            'The URL to the current shot for webcam 5',  
            default='http://webcam.oregonstate.edu/live/wavelab_current.jpg'
    )

    imgAddr_6 = dbsettings.StringValue(
            'Webcam 6 image address', 
            'The URL to the current shot for webcam 6',  
            default='http://webcam.oregonstate.edu/live/south_current.jpg'
    )

    imgAddr_7 = dbsettings.StringValue(
            'Webcam 7 image address', 
            'The URL to the current shot for webcam 7',  
            default='http://webcam.oregonstate.edu/live/gill_current.jpg'
    )

    imgAddr_8 = dbsettings.StringValue(
            'Webcam 8 image address', 
            'The URL to the current shot for webcam 8',  
            default='http://webcam.oregonstate.edu/live/andrews_current.jpg'
    )

    imgAddr_9 = dbsettings.StringValue(
            'Webcam 9 image address', 
            'The URL to the current shot for webcam 9',  
            default='http://webcam.oregonstate.edu/live/hmsc_current.jpg'
    )
        
    imgAddr_10 = dbsettings.StringValue(
            'Webcam 10 image address', 
            'The URL to the current shot for webcam 10',  
            default='http://webcam.oregonstate.edu/live/agate_current.jpg'
    )
        
    imgAddr_11 = dbsettings.StringValue(
            'Webcam 11 image address', 
            'The URL to the current shot for webcam 11',  
            default='http://webcam.oregonstate.edu/live/wecoma_current.jpg'
    )

    # =============
    #  tile titles
    # =============

    title_0 = dbsettings.StringValue(
            'Webcam 0 Title', 
            'The title for webcam 0', 
            default='Monroe Street'
    )

    title_1 = dbsettings.StringValue(
            'Webcam 1 Title', 
            'The title for webcam 1',  
            default='Reser Stadium'
    )

    title_2 = dbsettings.StringValue(
            'Webcam 2 Title', 
            'The title for webcam 2',  
            default='Memorial Union'
    )

    title_3 = dbsettings.StringValue(
            'Webcam 3 Title', 
            'The title for webcam 3',  
            default='Valley Library'
    )

    title_4 = dbsettings.StringValue(
            'Webcam 4 Title', 
            'The title for webcam 4',  
            default='Gloss Stadium'
    )

    title_5 = dbsettings.StringValue(
            'Webcam 5 Title', 
            'The title for webcam 5',  
            default='Wave Lab'
    )

    title_6 = dbsettings.StringValue(
            'Webcam 6 Title', 
            'The title for webcam 6',  
            default='South Campus'
    )

    title_7 = dbsettings.StringValue(
            'Webcam 7 Title', 
            'The title for webcam 7',  
            default='Gill Renovation'
    )

    title_8 = dbsettings.StringValue(
            'Webcam 8 Title', 
            'The title for webcam 8',  
            default='Andrews Forrest'
    )
    
    title_9 = dbsettings.StringValue(
            'Webcam 9 Title', 
            'The title for webcam 9',  
            default='Hatfield Marine Science'
    )
    
    title_10 = dbsettings.StringValue(
            'Webcam 10 Title', 
            'The title for webcam 10',  
            default='Agate Beach'
    )
    
    title_11 = dbsettings.StringValue(
            'Webcam 11 Title', 
            'The title for webcam 11',  
            default='Research Vessel WECOMA'
    )

webcams_settings = webcamsSettings('webcams Settings')
