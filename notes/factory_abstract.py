# an interface,
#   to create families of related objects,
#   without specifying the concrete class
# client is isolated from the creation of the objects,
#   but allowed to use them, access through an interface
from abc import ABCMeta, abstractmethod


class PizzaFactory(metaclass=ABCMeta):  # AbstractFactory, the interface
    # ensures code depends on interface, not implementation
    @abstractmethod
    def createVegPizza(self):  # createProduct()
        # NOTE one or more factory methods to create a family of related objects
        pass

    @abstractmethod
    def createNonVegPizza(self):  # createAnotherProduct()
        # NOTE one or more factory methods to create a family of related objects
        pass


class IndianPizzaFactory(PizzaFactory):  # ConcreteFactory1
    def createVegPizza(self):  # createProduct()
        return DeluxVeggiePizza()

    def createNonVegPizza(self):  # createAnotherProduct()
        return ChickenPizza()


class USPizzaFactory(PizzaFactory):  # ConcreteFactory2
    def createVegPizza(self):  # createProduct()
        return MexicanVegPizza()

    def createNonVegPizza(self):  # createAnotherProduct()
        return HamPizza()


class VegPizza(metaclass=ABCMeta):  # AbstractProduct
    @abstractmethod
    def prepare(self, VegPizza):
        pass


class NonVegPizza(metaclass=ABCMeta):  # AnotherAbstractProduct
    @abstractmethod
    def serve(self, VegPizza):
        pass


class DeluxVeggiePizza(VegPizza):  # ConcreteProduct1
    def prepare(self):
        print("prepare ", type(self).__name__)


class ChickenPizza(NonVegPizza):  # AnotherConcreteProduct1
    def serve(self, VegPizza):
        print(type(self).__name__, " is served with Chicken on ", type(VegPizza).__name__)


class MexicanVegPizza(VegPizza):  # ConcreteProduct2
    def prepare(self):
        print("Prepare ", type(self).__name__)


class HamPizza(NonVegPizza):  # AnotherConcreteProduct2
    def serve(self, VegPizza):
        print(type(self).__name__, " is served with Ham on ", type(VegPizza).__name__)


class PizzaStore:  # access interface
    def makePizzas(self):
        for factory in [IndianPizzaFactory(), USPizzaFactory()]:
            # NOTE creating different families of related objects
            self.factory = factory
            self.NonVegPizza = self.factory.createNonVegPizza()  # NOTE composition to create objects of other class
            self.VegPizza = self.factory.createVegPizza()  # NOTE composition to create objects of other class
            self.VegPizza.prepare()
            self.NonVegPizza.serve(self.VegPizza)

# client code
if __name__ == '__main__':
    pizza = PizzaStore()
    pizza.makePizzas()
