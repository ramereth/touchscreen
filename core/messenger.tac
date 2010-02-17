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
   

Starting Server:
   twistd -y messenger.tac
"""

from __future__ import with_statement

from twisted.web import server, resource
from twisted.application import service, internet
from twisted.internet import reactor
from twisted.internet.defer import Deferred
from threading import Lock

TIMEOUT = 1 # timeout in seconds
MESSAGE_QUEUES = {}
QUEUE_LOCK = Lock()

def get_queue(name):
    """
    Threadsafe Helper function for retreiving a queue.  If the queue does not
    exist yet it is created.
    """
    global MESSAGE_QUEUES
    global QUEUE_LOCK
    
    with QUEUE_LOCK:
        try:
            queue = MESSAGE_QUEUES[name]
        except:
            #queue doesn't exist, create it
            queue = {'messages':[], 'requests':[], 'lock':Lock()}
            MESSAGE_QUEUES[name] = queue
    return queue


class Simple(resource.Resource):
    isLeaf = True    

    def render_GET(self, request):

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

                queue = get_queue(queue_name)
                with queue['lock']:
                    # if there are waiting requests, process the first request
                    # that has not timed out.  otherwise queue the message
                    if queue['requests']:
                        waiting = queue['requests'].pop(0)
                        waiting.write(message)
                        waiting.finish()
                    else:
                        queue['messages'].append(message)
                # return success
                return '1'

            else:
                #get command, pop message out of the queue
                queue = get_queue(queue_name)
                with queue['lock']:
                    try:
                        return queue['messages'].pop(0)
                    except:
                        reactor.callLater(TIMEOUT, self.timeout, queue, request)
                        queue['requests'].append(request)
                        return server.NOT_DONE_YET
        except KeyError:
            #missing parameter, return error code
            return '-1'


    def timeout(self, queue, request):
        """
        Times out a request that waited too long for a message.  This is called
        using reactor.callLater(...) and must be called prior to the HTTP
        response timing out.  This lets the client handle the error in a
        better way since jquery ajax functions do not handle errors.
        """
        with queue['lock']:
            if not request.finished:
                request.write('0')
                request.finish()
                queue['requests'].remove(request)


def getMessageService():
    site = server.Site(Simple())
    return internet.TCPServer(9000, site)

#root application object
application = service.Application('Messaging Application')

# attach service
service = getMessageService()
service.setServiceParent(application)
