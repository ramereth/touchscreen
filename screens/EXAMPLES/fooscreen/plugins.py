from core.models import Screen, ScreenGeneralSettings
from django import forms


class FooSettings(forms.Form):
    text = forms.CharField(max_length=100, help_text='this text will show up in the box')


class Foo(Screen):
    template='foo.html'
    description='An example screen named FOO'
    config_form=(FooSettings, ScreenGeneralSettings)
    
    show='fade'
    hide='fade'