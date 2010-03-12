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
    js_init ='init',
    js_start='start',
    js_stop ='stop'
)


