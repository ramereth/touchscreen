# Dowloads the sponsors rss files for parsing by the template

# NOTE: This needs to be fixed to run every time this screen is
# displayed. Also, change hardcoded values to setting variables. ATM,
# it'll only successfully run when invoked via the command line.

import urllib

localFile = open( "sponsors.xml", 'w' )
remoteFile = urllib.urlopen( "http://osuosl.org/members/rss.xml" )
localFile.write( remoteFile.read() )
localFile.close()
remoteFile.close()
