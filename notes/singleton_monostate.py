# The Monostate (Borg, as Martellis calls it) Singleton pattern:
# [Alex Martelli]: author of Python in a Nutshell,
#   in contrast to GoF's opinion that for singletons there should be one and only one object,
#   suggests that coders should be bothered about the state and behavior rather than the identity.
# Borg pattern is about objects sharing the same state
# Borg affects subclasses, (unless explicitly overwrites __dict__), while Singletons don't
# Borg does not allow setting up attributes in __init__:
#   or it will get overwritten the next time a Borg instance is created,
#   causing subtle bugs


class Borg:
    __shared_state = {}

    def __init__(self):
        # explicitly assign all instances of Borg's __dict__ to a shared state
        self.__dict__ = self.__shared_state

if __name__ == '__main__':
    b = Borg()
    b1 = Borg()
    b.x = 4  # Affects all Borg instances, because of the shared __dict__ states
    print("Borg Object 'b': ", b)  # m and m1 are different objects
    print("Borg Object 'b1': ", b1)
    print("Object State 'b':", b.__dict__)  # m and m1 share the same state
    print("Object State 'b1':", b1.__dict__)


# another way to implement Borg:
class Borg2:
    __shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__shared_state
        return obj
