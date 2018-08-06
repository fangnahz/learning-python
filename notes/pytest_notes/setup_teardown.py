# coding: utf-8
# execute with command `py.test setup_teardown.py -s`
# where `-s` or `--capture=no` disables output (print) suppression


def setup_module(module):
    print('setting up MODULE {}'.format(module.__name__))


def teardown_module(module):
    print('tearing down MODULE {}'.format(module.__name__))


def test_a_function():
    print('RUNNING TEST FUNCTION')


class BaseTest:
    def setup_class(cls):
        print('setting up CLASS {}'.format(cls.__name__))

    def teardown_class(cls):
        print('tearing down CLASS {}'.format(cls.__name__))

    def setup_method(self, method):
        print('setting up METHOD {}'.format(method.__name__))

    def teardown_method(self, method):
        print('tearing down METHOD {}'.format(method.__name__))


class TestCalss(BaseTest):
    def test_mehtod_1(self):
        print('RUNNING METHOD 1-1')

    def test_mehtod_2(self):
        print('RUNNING METHOD 1-2')


class TestCalss2(BaseTest):
    def test_mehtod_1(self):
        print('RUNNING METHOD 2-1')

    def test_mehtod_2(self):
        print('RUNNING METHOD 2-2')
