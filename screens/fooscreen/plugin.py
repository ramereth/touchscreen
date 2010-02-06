from core.models import *
from models import foo_settings

"""
create instance of screens this plugin provides
"""
foo_screen = Screen(
    'foo.html',
    'FooScreen',

    #optional params
    duration=3000,
    settings=foo_settings,
    #hide='fade', 
    #show='fade',
    slideshow=True,
    js_init ='foo_screen_init',
    js_start='foo_screen_start',
    js_stop ='foo_screen_stop'
)


