import dbsettings

""" ================================================================
# General Settings
================================================================ """
class GeneralSettings(dbsettings.Group):
    DISPLAY_HEIGHT     = dbsettings.IntegerValue('Screen Height', 'Height of the display screen', default=768)
    DISPLAY_WIDTH      = dbsettings.IntegerValue('Screen Width','Width of the display screen', default=1360)
    MENU_HEIGHT        = dbsettings.IntegerValue('Menu Height', 'Height of the menu screen', default=768)
    MENU_WIDTH         = dbsettings.IntegerValue('Menu Width','Width of the menu screen', default=1024)
    DISPLAY_DURATION   = dbsettings.IntegerValue('Default Screen Duration', 'How long screens will be displayed', default=10000)
    TIMEOUT            = dbsettings.IntegerValue('Screen Timeout', 'Duration of time without activity before the slide show restarts', default=10000)
general_settings = GeneralSettings('General Settings')
