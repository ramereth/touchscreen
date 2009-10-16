"""
"curl" custom Django tag
Copyright (c) 2009 Oregon State Univerisity - info(at)osuosl.org | osuosl.org
licensed under GPLv3.
Date: 10/15/2009

@projectDescription A Django tag to "curl" a remote address into a template document. Works similarly to the Linux "curl" utility (see http://curl.haxx.se/). Usage: The tag {% curl "http://www.example.com" %} is replaced by the raw data from www.example.com.
@author Rob McGuire-Dale - rob@osuoslcom
@version 1.0

@param {string} The url of the remote file to curl, including the "http://" ( E.g. {% curl "http://www.example.com" %} )
@return {string} The raw data from the curl'd file
"""

from django import template
import urllib2

# register this as a "simple" Django tag
register = template.Library()
@register.simple_tag

# define curl function to return the raw data opened from the URL
def curl( url ):
    return urllib2.urlopen( url ).read()
