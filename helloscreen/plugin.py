from core.plugin_manager import *
from core.models import *

"""
Example screen #1
"""
'''
class HelloScreen(Screen):
    template='hello.html'
    name='HelloScreen'
    hash='HelloScreen'
'''
"""
Example screen #2
"""
'''
class WorldScreen(Screen):
    template='world.html'
    name='WorldScreen'
    hash='WorldScreen'
'''

hello_screen = Screen('world.html', 'WorldScreen')
