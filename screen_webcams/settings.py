import dbsettings


""" ================================================================
# Settings for screen_webcams
================================================================ """
class screen_webcamsSettings( dbsettings.Group ):
    ADDR_1     = dbsettings.StringValue('Thumbnail 1 image address', 'The image address of thumbnail 1', default='http://webcam.oregonstate.edu/live/andrews_current.jpg')

screen_webcams_settings = screen_webcamsSettings('screen_webcams Settings')
