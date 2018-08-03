# Simple Server
import socket
import gzip
from io import BytesIO
import time


def respond(client):
    response = input("Enter a value: ")
    client.send(bytes(response, 'utf-8'))
    client.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 2401))
server.listen(1)
try:
    while True:
        client, addr = server.accept()
        respond(client)
finally:
    server.close()
# Simple Client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 2401))
print("Received: {0}".format(client.recv(1024)))  # stops and waits for response
client.close()


# Log Socket
class LogSocket:

    def __init__(self, socket):
        self.socket = socket

    def send(self, data):
        print("Sending {0} to {1}".format(data, self.socket.getpeername()[0]))
        self.socket.send(data)

    def close(self):
        self.socket.close()


# Log Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 2401))
server.listen(1)
try:
    while True:
        client, addr = server.accept()
        respond(LogSocket(client))
finally:
    server.close()


# Zip Socket
class GzipSocket:

    def __init__(self, socket):
        self.socket = socket

    def send(self, data):
        buf = BytesIO()
        zipfile = gzip.GzipFile(fileobj=buf, mode="w")
        zipfile.write(data)
        zipfile.close()
        self.socket.send(buf.getvalue())

    def close(self):
        self.socket.close()

log_send = 'Bool type: if logs should be kept'
compress_hosts = ['hosts', 'requires', 'compression']
# log/Zip Server
client, addr = server.accept()
if log_send:
    client = LogSocket(client)
if client.getpeername()[0] in compress_hosts:
    client = GzipSocket(client)
respond(client)


# function call logging decorater
def log_calls(func):
    def wrapper(*args, **kwargs):
        now = time.time()
        print("calling {0} with {1} and {2}".format(func.__name__, args, kwargs))
        return_value = func(*args, **kwargs)
        print("Executed {0} in {1}ms".format(func.__name__, time.time() - now))
        return return_value
    return wrapper


def test1(a, b, c):
    print("\ttest1 called")


def test2(a, b):
    print("\ttest2 called")


def test3(a, b):
    print("\ttest3 called")
    time.sleep(1)

test1 = log_calls(test1)
test2 = log_calls(test2)
test3 = log_calls(test3)

test1(1, 2, 3)
test2(4, b=5)
test3(6, 7)
