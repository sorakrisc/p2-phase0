#!/usr/bin/python
import thread
import time
import sys
import socket as skt
from urlparse import urlparse

def parse_url(url, DEFAULT_PORT=80):
    """ Parse a given url into host, path, and port.
        Use DEFAULT_PORT (80) if unspecified.
    """
    parsed_url = urlparse(url)
    host, path, port = (parsed_url.hostname,
                        parsed_url.path,
                        parsed_url.port)
    if not port:
        port = DEFAULT_PORT
    return (host, path, port)

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print "Starting " + self.name
        #my class
        #print_time(self.name, self.counter, 5)
        print "Exiting " + self.name

class punch(object):
    def __init__(self, url):
        # Create a TCP socket to host at the right port
        self.client_socket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
        self.client_socket.connect((host, port))

        self.url = url
        self.host = host
        self.path = path
        self.port = port
        self.main()
    def send_request(self):
            # Make an initial request & deliver it
            request = make_request('GET', self.path,
                {'Host': self.host,
                 'Connection': 'close'}
            )
            self.client_socket.send(request)
    def main(self):
        #run with the amount got using loop?
        # is loop fast enough?

if __name__ = __main__:
    for i in range(5):
        thread_name = "Thread-"+str(i+1)
        thread = myThread(i+1, thread_name, i+1)
        thread.start()
