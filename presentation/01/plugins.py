from core.models import *

class AboutGeneralSettingsForm(ScreenGeneralSettings):
    DISPLAY_DURATION = forms.IntegerField(
        label='Default Screen Duration',
        help_text='How long screens will be displayed',
        initial=300000
    )


class slide_01(Screen):
    description = ''
    template = '01.html' # the screen's file name
