import subprocess
import socket
import pytest
import time


@pytest.fixture
def echoserver(request):
    def setup():
        p = subprocess.Popen(
            ['python3', 'echo_server.py']
        )
        time.sleep(1)
        return p

    def cleanup(p):
        p.terminate()

    return request.cached_setup(
        setup=setup,
        teardown=cleanup,
        scope='session'  # 'function', 'module'
    )


@pytest.fixture
def clientsocket(request):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 1028))
    request.addfinalizer(lambda: s.close())
    return s


def test_echo(echoserver, clientsocket):
    clientsocket.send(b'abc')
    assert clientsocket.recv(3) == b'abc'


def test_echo2(echoserver, clientsocket):
    clientsocket.send(b'def')
    assert clientsocket.recv(3) == b'def'
