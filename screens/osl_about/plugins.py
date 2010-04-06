from core.models import *


class AboutGeneralSettingsForm(ScreenGeneralSettings):
    DISPLAY_DURATION = forms.IntegerField(
        label='Default Screen Duration',
        help_text='How long screens will be displayed',
        initial=300000
    )


class screens_osl_about(Screen):
    description = 'Screen displaying generation information about the open source lab'
    template = 'osl_about.html' # the screen's file name

