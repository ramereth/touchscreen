from django.db import models
import dbsettings

""" ================================================================
# Settings for fooscreen
================================================================ """
class FooScreenSettings(dbsettings.Group):
    TEXT     = dbsettings.StringValue('box test', 'Text that will be displayed in the fooscreen box', default='This box was drawn by fooscreen')
foo_settings = FooScreenSettings('Foo Screen Settings')
