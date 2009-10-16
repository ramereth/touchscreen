from django import template
import urllib2

register = template.Library()

@register.simple_tag
def curl( url ):
    remotefile = urllib2.urlopen( url )
    return remotefile.read()
