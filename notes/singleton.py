# Creational pattern
# To have only one object of a given type,
#   with a global point of access,
#   to avoid conflicting requests on the same resource
# Used for:
#   * logging: across multiple services for sequential logs
#   * db oprations: to maintain data consistency
#   * printer spoolers, thread pools, caches, dialog boxes, registry settings, etc
# to reduce resource use
# But keep in mind, in Python Singleton is almost always an anti-pattern

# All modules are Singletons by default because of Python's importing behavior
# Python...
#   1. Checks whether a module has been imported
#   2. If imported, returns the boject of the module. If not, imports and instantiates it
#   3. When imported again, it's not initialized again, only returns the same previous object

# Drawbacks due to the global point of access
# * Global variables get changed by mistake
# * Multiple references may get created to the same object
# * All classes dependent on global variables get tightly coupled


class OneOnly:
    _singleton = None

    def __new__(cls, *args, **kwargs):
        # [Guido]: __new__ is a static method, not a class method.
        #   I initially thought it would have to be a class method,
        #   and that's why I added the classmethod primitive.
        #   Unfortunately, with class methods, upcalls don't work right in this case,
        #   so I had to make it a static method with an explicit class as its first argument.
        # @staticmethod can be added, or not
        if not cls._singleton:
            cls._singleton = super(OneOnly, cls).__new__(cls, *args, **kwargs)
            # __new__ being static method allows a use-case
            #   when you create an instance of the derived class in it (the derived class):
            #   return super(<derived_class>, derived_cls).__new__(derived_cls, *args, **kwargs)
            # If __new__ is a class method then the above is written as:
            #   return super(<derived_class>, derived_cls).__new__(*args, **kwargs)
            #   and there is no place to put derived_cls
            # Confusions occur, if using class method instead of static method,
            #   when you try to call base __new__ without using super,
            #   in which case the result is not an instance of the base class, but the derived
            #   * but of course, this is a very esoteric feature may be useful in esoteric cases
        return cls._singleton


class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


# Lazy instantiation of singleton refers to the following snippet
class LazySingleton:
    __instance = None

    def __init__(self):
        # When __init__ is called, but no new object gets created
        #   This is to reduce resource used on inits
        if not LazySingleton.__instance:
            print('LazySingleton __init__ method called..')
        else:
            print('LazySingleton instance already created:', self.get_instance())

    @classmethod
    def get_instance(cls):
        # New instance is created only when needed,
        #   rather than right on initializations
        # If lazy instantiation is not required, implement __call__ is another choice
        if not cls.__instance:
            cls.__instance = LazySingleton()
        return cls.__instance


if __name__ == '__main__':
    s = Singleton()
    print('Object created', s)
    s1 = Singleton()
    print('object created', s1)
    s_lazy = LazySingleton()  # LazySingleton class initialized, but object not created
    print('LazySingleton object created', LazySingleton.get_instance())  # Object gets created
    s1_lazy = LazySingleton()  # LazySingleton instance already created
