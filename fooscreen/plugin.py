from core.models import *

"""
create instance of screens this plugin provides
"""
foo_screen = Screen(
                    'foo.html',
                    'FooScreen',
                    hide='fade', 
                    show='fade',
                    js_init ='foo_screen_init',
                    js_start='foo_screen_start',
                    js_stop ='foo_screen_stop',)


