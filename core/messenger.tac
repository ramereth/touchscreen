# You can run this .tac file directly with:
#    twistd -ny messenger.tac

"""
Simple Messaging Daemon.  It allows multiple queues of messages to be added to and retrieved.

Uses http GET requests

Parameters:
   c = 1 for send,  0 for retrieve.
   q = queue name to send to or retrieve from
   m = message to queue, only required for send

Example:
   http://localhost:9000/?c=1&q=foo_queue&m=bar_message
   http://localhost:9000/?c=0&q=foo_queue
"""

from __future__ import with_statement

from twisted.web import server, resource
from twisted.application import service, internet
from threading import Lock

MESSAGE_QUEUES = {}
QUEUE_LOCK = Lock()

class Simple(resource.Resource):
    isLeaf = True

    def render_GET(self, request):
        global MESSAGE_QUEUES
        global QUEUE_LOCK

        try:
            command = int(request.args['c'][0])
            queue_name = request.args['q'][0]

            if command:
                # its a send command, record message
                try:
                    message = request.args['m'][0]
                except KeyError:
                    #missing parameter, return error code
                    return '-1'

                try:
                    queue = MESSAGE_QUEUES[queue_name]
                except:
                    #queue doesn't exist, create it
                    queue = {'messages':[], 'lock':Lock()}

                    with QUEUE_LOCK:
                        MESSAGE_QUEUES[queue_name] = queue

                with  queue['lock']:
                    queue['messages'].append(message)

                # return success
                return '1'

            else:
                #get command, pop message out of the queue
                try:
                    queue = MESSAGE_QUEUES[queue_name]

                    with queue['lock']:
                        message = queue['messages'].pop(0)

                except (IndexError,KeyError):
                    #empty or uninitialized queue, return 0
                    return '0'

                return message

        except KeyError:
            #missing parameter, return error code
            return '-1'

def getMessageService():
    site = server.Site(Simple())
    return internet.TCPServer(9000, site)

#root application object
application = service.Application('Messaging Application')

# attach service
service = getMessageService()
service.setServiceParent(application)