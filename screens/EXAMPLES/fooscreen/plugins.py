from core.models import Screen, ScreenGeneralSettings
from django import forms


class FooSettings(forms.Form):
    text = forms.CharField(
                label = 'text value',
                initial = 'Enter some text',
                help_text='the value you enter will be used in the template',
                max_length=100
                )


class Foo(Screen):
    template='foo.html'
    description='An example screen named FOO'
    config_form=(FooSettings, ScreenGeneralSettings)
    
    show='fade'
    hide='fade'