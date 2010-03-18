# You can run this .tac file directly with:
#    twistd -ny messenger.tac

"""
Simple Messaging Daemon.  It allows multiple queues of messages to be added to
and retrieved.  It allows multiple clients to receive messages.

Uses http GET requests

Parameters:
   c = 0 for receive, 1 for send,  2 for clear user's queue
   q = queue name to send to or retrieve from
   m = message to queue (only required for send)
   u = user requesting message (only required for receive)

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

TIMEOUT = 240 # request timeout in seconds
CLIENT_TIMEOUT = TIMEOUT + 30
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
            queue = {'clients':{}, 'requests':{}, 'timeouts':{}, 'lock':Lock()}
            MESSAGE_QUEUES[name] = queue
    return queue


class Simple(resource.Resource):
    isLeaf = True    

    def render_POST(self, request):
        return self.render_GET(request)

    def render_GET(self, request):
        args = request.args
        if 'c' in args and 'q' in args and 'u' in args:
            command = int(args['c'][0])
            queue_name = args['q'][0]
            client = args['u'][0]
            queue = get_queue(queue_name)
            request.setHeader('Access-Control-Allow-Origin','*')
            
            with queue['lock']:
                # setup client timeout.  reset existing timeout if it exists
                if client in queue['timeouts']:
                    queue['timeouts'][client].reset(CLIENT_TIMEOUT)
                else:
                    queue['timeouts'][client] = reactor.callLater( \
                                                        CLIENT_TIMEOUT, \
                                                        self.client_timeout, \
                                                        queue, client)
                if command == 1:
                    # its a send command, record message
                    try:
                        message = args['m'][0]
                    except KeyError:
                        #missing parameter, return error code
                        return '-1'
                    
                    # if there are clients waiting for requests process those
                    # immediately.  queue the message for all other clients
                    clients = queue['clients'].keys()
                    for waiting in queue['requests'].values():
                        waiting.write(message)
                        waiting.finish()
                        clients.remove(waiting.args['u'][0])
                    queue['requests'] = {}
                    
                    for client in clients: 
                        queue['clients'][client].append(message)
                    # return success
                    return '1'

                elif command == 0:
                    #get command, pop message out of the queue
                    if not client in queue['clients']:
                        queue['clients'][client]=[]
                    try:
                        return queue['clients'][client].pop(0)
                    except:
                        reactor.callLater(TIMEOUT, self.timeout, queue, request)
                        queue['requests'][client]=request
                        return server.NOT_DONE_YET
            
                elif command == 2:
                    #clear queue
                    queue['clients'][client] = []
                return '1'
            
        else:
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
                if request.args['u'][0] in queue['requests']:
                    del queue['requests'][request.args['u'][0]]

    def client_timeout(self, queue, client):
        """
        Times out an inactive client.  any messages it hasn't consumed yet are
        destroyed.
        """
        with queue['lock']:
            if client in queue['clients']:
                del queue['clients'][client]
            if client in queue['requests']:
                del queue['requests'][client]
            del queue['timeouts'][client]


def getMessageService():
    site = server.Site(Simple())
    return internet.TCPServer(9000, site)

#root application object
application = service.Application('Messaging Application')

# attach service
service = getMessageService()
service.setServiceParent(application)
