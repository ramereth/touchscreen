from core.models import Screen, ScreenGeneralSettings
from django import forms


class WebcamsSettings(forms.Form):

    # ==================
    #  general settings
    # ==================
    
    imgRefreshInterval = forms.IntegerField(
            label='Image Refresh Interval', 
            help_text='The time interval to refresh the images, in milliseconds', 
            initial=30000
    )

    # =====================
    #  image size settings
    # =====================

    thumbnail_height = forms.IntegerField(
            label='Thumbnail Image Height', 
            help_text='The height of the thumbnail images', 
            initial=120
    )
    
    thumbnail_width = forms.IntegerField(
            label='Thumbnail Image Width', 
            help_text='The width of the thumbnail images', 
            initial=160
    )
    
    mainTile_height = forms.IntegerField(
            label='Main Tile Image Height', 
            help_text='The height of the main tile\'s image', 
            initial=480
    )
    
    mainTile_width = forms.IntegerField(
            label='Main Tile Image Width', 
            help_text='The width of the main tile\'s image', 
            initial=640
    )

    # =================
    #  image addresses
    # =================

    imgAddr_0 = forms.CharField(
            label='Webcam 0 image address', 
            help_text='The URL to the current shot for webcam 0', 
            initial='http://webcam.oregonstate.edu/live/monroe_current.jpg'
    )

    imgAddr_1 = forms.CharField(
            label='Webcam 1 image address', 
            help_text='The URL to the current shot for webcam 1', 
            initial='http://webcam.oregonstate.edu/live/reser1_current.jpg'
    )

    imgAddr_2 = forms.CharField(
            label='Webcam 2 image address', 
            help_text='The URL to the current shot for webcam 2',  
            initial='http://webcam.oregonstate.edu/live/mu_current.jpg'
    )

    imgAddr_3 = forms.CharField(
            label='Webcam 3 image address', 
            help_text='The URL to the current shot for webcam 3', 
            initial='http://webcam.oregonstate.edu/live/library_current.jpg'
    )

    imgAddr_4 = forms.CharField(
            label='Webcam 4 image address', 
            help_text='The URL to the current shot for webcam 4',  
            initial='http://webcam.oregonstate.edu/live/baseball_current.jpg'
    )

    imgAddr_5 = forms.CharField(
            label='Webcam 5 image address', 
            help_text='The URL to the current shot for webcam 5',  
            initial='http://webcam.oregonstate.edu/live/wavelab_current.jpg'
    )

    imgAddr_6 = forms.CharField(
            label='Webcam 6 image address', 
            help_text='The URL to the current shot for webcam 6',  
            initial='http://webcam.oregonstate.edu/live/south_current.jpg'
    )

    imgAddr_7 = forms.CharField(
            label='Webcam 7 image address', 
            help_text='The URL to the current shot for webcam 7',  
            initial='http://webcam.oregonstate.edu/live/gill_current.jpg'
    )

    imgAddr_8 = forms.CharField(
            label='Webcam 8 image address', 
            help_text='The URL to the current shot for webcam 8',  
            initial='http://webcam.oregonstate.edu/live/andrews_current.jpg'
    )

    imgAddr_9 = forms.CharField(
            label='Webcam 9 image address', 
            help_text='The URL to the current shot for webcam 9',  
            initial='http://webcam.oregonstate.edu/live/hmsc_current.jpg'
    )
        
    imgAddr_10 = forms.CharField(
            label='Webcam 10 image address', 
            help_text='The URL to the current shot for webcam 10',  
            initial='http://webcam.oregonstate.edu/live/agate_current.jpg'
    )
        
    imgAddr_11 = forms.CharField(
            label='Webcam 11 image address', 
            help_text='The URL to the current shot for webcam 11',  
            initial='http://webcam.oregonstate.edu/live/wecoma_current.jpg'
    )

    # =============
    #  tile titles
    # =============

    title_0 = forms.CharField(
            label='Webcam 0 Title', 
            help_text='The title for webcam 0', 
            initial='Monroe Street'
    )

    title_1 = forms.CharField(
            label='Webcam 1 Title', 
            help_text='The title for webcam 1',  
            initial='Reser Stadium'
    )

    title_2 = forms.CharField(
            label='Webcam 2 Title', 
            help_text='The title for webcam 2',  
            initial='Memorial Union'
    )

    title_3 = forms.CharField(
            label='Webcam 3 Title', 
            help_text='The title for webcam 3',  
            initial='Valley Library'
    )

    title_4 = forms.CharField(
            label='Webcam 4 Title', 
            help_text='The title for webcam 4',  
            initial='Goss Stadium'
    )

    title_5 = forms.CharField(
            label='Webcam 5 Title', 
            help_text='The title for webcam 5',  
            initial='Wave Lab'
    )

    title_6 = forms.CharField(
            label='Webcam 6 Title', 
            help_text='The title for webcam 6',  
            initial='South Campus'
    )

    title_7 = forms.CharField(
            label='Webcam 7 Title', 
            help_text='The title for webcam 7',  
            initial='Gill Annex'
    )

    title_8 = forms.CharField(
            label='Webcam 8 Title', 
            help_text='The title for webcam 8',  
            initial='Andrews Forrest'
    )
    
    title_9 = forms.CharField(
            label='Webcam 9 Title', 
            help_text='The title for webcam 9',  
            initial='Hatfield Marine Science'
    )
    
    title_10 = forms.CharField(
            label='Webcam 10 Title', 
            help_text='The title for webcam 10',  
            initial='Agate Beach'
    )
    
    title_11 = forms.CharField(
            label='Webcam 11 Title', 
            help_text='The title for webcam 11',  
            initial='Research Vessel WECOMA'
    )


class Webcams(Screen):
    template='webcams.html'
    description='still images from webcams around campus'

    #optional params
    config_form=(WebcamsSettings, ScreenGeneralSettings)