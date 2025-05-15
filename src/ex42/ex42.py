## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a class
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## Cat is-a class
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Person is-a class
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name

       ## Person has-a pet of some kind
        self.pet = None

## Employee is-a class
class Employee(Person):

    def __init__(self, name, salary):
        ## inheritance magic
        super(Employee, self).__init__(name)
        ## Employee has a salary
        self.salary = salary

## Fish is-a class
class Fish(object):
    pass

## Salmon is-a class
class Salmon(Fish):
    pass

## Halibut is-a class
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet satan
mary.pet = satan

## frank is-a employee
frank = Employee("Frank", 120000)

## frank has-a pet rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is a Salmon
crouse = Salmon()

## harry is a Halibut
harry = Halibut()
