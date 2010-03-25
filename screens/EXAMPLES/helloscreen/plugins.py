from core.models import Screen, ScreenGeneralSettings
from django import forms


class HelloScreen(Screen):
    template='hello.html'
    description='An example screen named Hello'


class WorldScreen(Screen):
    template='world.html'
    description='An example screen named world'    
