# subclass of factory is responsible for object creation
# create through inheritance, not instantiation
# can return same instance or subclass,
#   rather than an object of a type
#   (as is the case in simple factory)
from abc import ABCMeta, abstractmethod


class Section(metaclass=ABCMeta):  # Product
    @abstractmethod
    def describe(self):
        # This abstraction ensures factory depends on interface of Product,
        #   not the implementation of ConcreateProduct
        pass


class PersonalSection(Section):  # ConcreteProduct
    def describe(self):
        print("Personal Section")


class AlbumSection(Section):  # ConcreteProduct
    def describe(self):
        print("Album Section")


class PatentSection(Section):  # ConcreteProduct
    def describe(self):
        print("Patent Section")


class PublicationSection(Section):  # ConcreteProduct
    def describe(self):
        print("Publication Section")


class Profile(metaclass=ABCMeta):  # Creator
    def __init__(self):
        self.sections = []
        self.createProfile()

    @abstractmethod
    def createProfile(self):  # factoryMethod()
        # NOTE use inheritance and subclasses to decide which object to create
        pass

    def getSections(self):
        return self.sections

    def addSections(self, section):
        self.sections.append(section)


class linkedin(Profile):  # ConcreteCreator
    def createProfile(self):  # factoryMethod()
        # NOTE expose this function to user to create objects
        # NOTE used to create one product
        # The following code creating objects
        #   is separated from the client code,
        #   easy to add types with low maintenance
        self.addSections(PersonalSection())  # NOTE use inheritance and subclasses to decide which object to create
        self.addSections(PatentSection())  # NOTE use inheritance and subclasses to decide which object to create
        self.addSections(PublicationSection())  # NOTE use inheritance and subclasses to decide which object to create


class facebook(Profile):  # ConcreteCreator
    def createProfile(self):  # factoryMethod()
        # NOTE expose this function to user to create objects
        # NOTE used to create one product
        self.addSections(PersonalSection())  # NOTE use inheritance and subclasses to decide which object to create
        self.addSections(AlbumSection())  # NOTE use inheritance and subclasses to decide which object to create


# client code
if __name__ == '__main__':
    profile_type = input("Which Profile you'd like to create? [LinkedIn or FaceBook]")
    profile = eval(profile_type.lower())()
    print("Creating Profile..", type(profile).__name__)
    print("Profile has sections --", profile.getSections())
