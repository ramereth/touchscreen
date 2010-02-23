from core.models import *

"""
create instance of screens this plugin provides
"""
hello_screen = Screen('hello.html',
                    'HelloScreen',
                    js_init ='init',
                    js_start='start',
                    js_stop ='stop')


world_screen = Screen('world.html',
                    'WorldScreen',
                    js_init ='init',
                    js_start='start',
                    js_stop ='stop')

