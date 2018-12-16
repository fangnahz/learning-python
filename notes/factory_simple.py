# Factory: creational pattern
#   A class that creates objects of other types
#   Client calls factory method with parameters, get objects of desired types
# Why indirectly create using a factory?
#   * loose coupling: object creation independent of class implementation
#   * client only needs to know interace, simpler to implement
#       (no need to know object classes, methods)
#   * adding other types is easy, client needs not change (maybe another parameter)
#   * reuse existing types (if client directly create, a new object is always created)
# Variants:
#   * Simple Factory pattern
#   * Factory method pattern
#       subclasses decide the class for object creation
#   * Abstract Factory pattern
#       provides objects of another factory, thus hide object classes
from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    @abstractmethod
    def do_say(self):
        pass


class Dog(Animal):
    def do_say(self):
        print("Bhow Bhow!!")


class Cat(Animal):
    def do_say(self):
        print("Meow Meow!!")


# factory
class ForestFactory:
    def make_sound(self, object_type):
        return eval(object_type)().do_say()


# client code
if __name__ == '__main__':
    ff = ForestFactory()
    animal = input('Which animal should make_sound Dog or Cat?')
    ff.make_sound(animal)
