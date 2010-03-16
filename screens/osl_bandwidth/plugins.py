from core.models import Screen, ScreenGeneralSettings
from django import forms


class OSL_BandwidthSettings(forms.Form):

    # ==================
    #  general settings
    # ==================
    
    imgRefreshInterval = forms.IntegerField(
            label='Image Refresh Interval', 
            help_text='The time interval to refresh the images, in milliseconds', 
            initial=30000
    )

    # =====================
    #  tile size settings
    # =====================

    thumbnail_img_height = forms.IntegerField(
            label='Thumbnail Image Height', 
            help_text='The height of the thumbnail images', 
            initial=82
    )
    
    thumbnail_img_width = forms.IntegerField(
            label='Thumbnail Image Width', 
            help_text='The width of the thumbnail images', 
            initial=200
    )
    
    mainTile_height = forms.IntegerField(
            label='Main Tile Image Height', 
            help_text='The height of the main tile\'s images', 
            initial=202
    )
    
    mainTile_width = forms.IntegerField(
            label='Main Tile Image Width',
            help_text='The width of the main tile\'s images', 
            initial=495
    )

    # ===========================
    #  image address and titles
    # ===========================    
    title_0 = forms.CharField(
            label='Tile 0\'s Title', 
            help_text='The title of the 0th tile', 
            initial='Apache',
            max_length=128
    )
    
    imgAddr_0a = forms.CharField(
            label='Tile 0\'s 1st Image Address', 
            help_text='Source image address of the 0th tile\'s 1st image', 
            initial='http://netfoo.nero.net/netviewer/img/OSUOSL-Apache-Normal-day-ifInOctets-100000000000-AVERAGE.png',
            max_length=128
    )
    
    imgAddr_0b = forms.CharField(
            label='Tile 0\'s 2nd Image Address', 
            help_text='Source image address of the 0th tile\'s 2nd image', 
            initial='http://netfoo.nero.net/netviewer/img/OSUOSL-Apache-Normal-week-ifInOctets-100000000000-AVERAGE.png',
            max_length=128
    )
    
    title_1 = forms.CharField(
            label='Tile 1\'s Title', 
            help_text='The title of the 1st tile', 
            initial='Gentoo',
            max_length=128
    )
    
    imgAddr_1a = forms.CharField(
            label='Tile 1\'s 1st Image Address', 
            help_text='Source image address of the 1st tile\'s 1st image', 
            initial='http://netfoo.nero.net/netviewer/img/OSUOSL-Gentoo-Normal-day-ifInOctets-100000000000-AVERAGE.png',
            max_length=128
    )
    
    imgAddr_1b = forms.CharField(
            label='Tile 1\'s 2nd Image Address', 
            help_text='Source image address of the 1st tile\'s 2nd image', 
            initial='http://netfoo.nero.net/netviewer/img/OSUOSL-Gentoo-Normal-week-ifInOctets-100000000000-AVERAGE.png',
            max_length=128
    )
    
    title_2 = forms.CharField(
            label='Tile 2\'s Title', 
            help_text='The title of the 2nd tile', 
            initial='Kernel.org',
            max_length=128
    )
    
    imgAddr_2a = forms.CharField(
            label='Tile 2\'s 1st Image Address', 
            help_text='Source image address of the 2nd tile\'s 1st image', 
            initial='http://netfoo.nero.net/netviewer/img/OSUOSL-Kernel-Normal-day-ifInOctets-100000000000-AVERAGE.png',
            max_length=128
    )
    
    imgAddr_2b = forms.CharField(
            label='Tile 2\'s 2nd Image Address', 
            help_text='Source image address of the 2nd tile\'s 2nd image', 
            initial='http://netfoo.nero.net/netviewer/img/OSUOSL-Kernel-Normal-week-ifInOctets-100000000000-AVERAGE.png',
            max_length=128
    )
    
    title_3 = forms.CharField(
            label='Tile 3\'s Title', 
            help_text='The title of the 3rd tile', 
            initial='OpenOffice.org',
            max_length=128
    )
    
    imgAddr_3a = forms.CharField(
            label='Tile 3\'s 1st Image Address', 
            help_text='Source image address of the 3rd tile\'s 1st image', 
            initial='http://netfoo.nero.net/netviewer/img/OSUOSL-OpenOffice-Normal-day-ifInOctets-100000000000-AVERAGE.png',
            max_length=128
    )
    
    imgAddr_3b = forms.CharField(
            label='Tile 3\'s 2nd Image Address', 
            help_text='Source image address of the 3rd tile\'s 2nd image', 
            initial='http://netfoo.nero.net/netviewer/img/OSUOSL-OpenOffice-Normal-week-ifInOctets-100000000000-AVERAGE.png'
    )
    
    title_4 = forms.CharField(
            label='Tile 4\'s Title', 
            help_text='The title of the 4th tile', 
            initial='Mozilla'
    )
    
    imgAddr_4a = forms.CharField(
            label='Tile 4\'s 1st Image Address', 
            help_text='Source image address of the 4th tile\'s 1st image', 
            initial='http://netfoo.nero.net/netviewer/img/OSUOSL-Mozilla-Normal-day-ifInOctets-100000000000-AVERAGE.png',
            max_length=128
    )
    
    imgAddr_4b = forms.CharField(
            label='Tile 4\'s 2nd Image Address', 
            help_text='Source image address of the 4th tile\'s 2nd image', 
            initial='http://netfoo.nero.net/netviewer/img/OSUOSL-Mozilla-Normal-week-ifInOctets-100000000000-AVERAGE.png',
            max_length=128
    )
    
    title_5 = forms.CharField(
            label='Tile 5\'s Title', 
            help_text='The title of the 5th tile', 
            initial='OSL Services',
            max_length=128
    )
    
    imgAddr_5a = forms.CharField(
            label='Tile 5\'s 1st Image Address', 
            help_text='Source image address of the 5th tile\'s 1st image', 
            initial='http://netfoo.nero.net/netviewer/img/OSUOSL-Services-Normal-day-ifInOctets-100000000000-AVERAGE.png',
            max_length=128
    )
    
    imgAddr_5b = forms.CharField(
            label='Tile 5\'s 2nd Image Address', 
            help_text='Source image address of the 5th tile\'s 2nd image', 
            initial='http://netfoo.nero.net/netviewer/img/OSUOSL-Services-Normal-week-ifInOctets-100000000000-AVERAGE.png',
            max_length=128
    )


class OSLBandwidth(Screen):
    template='osl_bandwidth.html'
    description='Graphs of OSL bandwidth'

    #optional params
    config_form=(OSL_BandwidthSettings, ScreenGeneralSettings)
    js_init ='init'
    js_start='start'
    js_stop ='stop'
    js_onWinResize = 'onWinResize'

