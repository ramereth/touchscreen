from core.models import *

"""
create instance of screens this plugin provides
"""
hello_screen = Screen('hello.html',
                    'HelloScreen',
                    js_init ='hello_screen_init',
                    js_start='hello_screen_start',
                    js_stop ='hello_screen_stop')


world_screen = Screen('world.html',
                    'WorldScreen',
                    js_init ='world_screen_init',
                    js_start='world_screen_start',
                    js_stop ='world_screen_stop')

