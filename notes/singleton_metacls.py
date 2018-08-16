# About metaclasses:
# A metaclass is a class of a class
# e.g.: int (as well as all user defined classes) is a class of class 'type'
# >>> type(int)
# <class 'type'>
# when create class with `class A`, Python creates it by:
#   A = type(
#       name,  # name of the class
#       base,  # base class
#       dict  # attribute variable
#   )
# with a predifined meta class, e.g. MyKls, Python creates the class by:
#   A = MyKls(name, base, dict)
# To control the creation and initialization of a class,
#   metaclasses override the __new__ and __init__ methods


class MyInt(type):
    def __call__(cls, *args, **kwargs):
        print("***** Here's My int *****", args)
        print("Now do whatever you want with these objects...")
        return type.__call__(cls, *args, **kwargs)


class int(metaclass=MyInt):
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Now, singleton with metaclasses


class MetaSingleton(type):
    _instances = {}  # keeps all singletons (in a project)

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=MetaSingleton):
    pass

# however, before you absolutely sure you need a costum metaclass,
# the following snippet is just as good for singletons,
# just inherit your singletons from this one
_instances = {}


class Singleton:
    def __new__(cls, *args, **kwargs):
        if cls not in _instances:
            instance = super().__new__(cls)
            _instances[cls] = instance
        return _instances[cls]


if __name__ == '__main__':
    i = int(4, 5)

    logger1 = Logger()
    logger2 = Logger()
    print(logger1, logger2)
