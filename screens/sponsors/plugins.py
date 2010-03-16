from core.models import Screen, ScreenGeneralSettings
from django import forms


class OSLSponsorsSettings(forms.Form):
    sponsors_URL = forms.CharField(
        label='OSL Sponsors RSS Feed URL',
        help_text='URL of the RSS feed of the OSL sponsors.',
        initial='http://osuosl.org/members/rss.xml',
        max_length=128
    )
    
    friends_URL = forms.CharField(
        label='OSL Friends Page URL',
        help_text='URL of the page listing the friends of the OSL.',
        initial='http://osuosl.org/friends/members',
        max_length=128
    )

    friends_width = forms.IntegerField(
        label='Friends Tile Width',
        help_text='The friends tile width. Will NOT dynamically resize with screen.',
        initial=150)
        
    sponsors_max_width = forms.IntegerField(
        label='Sponsors Tile Maximum Width',
        help_text='The sponsors tile maximum width. Will dynamically resize if the width of the sponsors and friends tiles exceeds that of the browser window.',
        initial=750)
        
    friends_scroll_interval = forms.IntegerField(
        label='Friends Scroll Interval',
        help_text='Time between scrolling of a friend (in milliseconds). Must be at least 50 greater than scroll speed.',
        initial=3000)
    
    friends_scroll_speed = forms.IntegerField(
        label='Friends Scroll Speed',
        help_text='Time it takes to scroll a single item (in milliseconds). Must be at least 50 less than scroll interval.',
        initial=1000)
        
    sponsors_scroll_interval = forms.IntegerField(
        label='Sponsors Scroll Interval',
        help_text='Time between scrolling of a sponsor (in milliseconds). Must be at least 50 greater than scroll speed.',
        initial=10000)
        
    sponsors_scroll_speed = forms.IntegerField(
        label='Sponsors Scroll Speed',
        help_text='Time it takes to scroll a single item (in milliseconds). Must be at least 50 less than scroll interval.',
        initial=2000)


class OSL_Donors(Screen):
    template = 'sponsors.html'
    description = 'Open Source Lab sponsors'

    #optional params
    config_form = (OSLSponsorsSettings, ScreenGeneralSettings)