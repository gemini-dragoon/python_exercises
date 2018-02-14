## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    #pass
    print "Animal: "

## ??
class Dog(Animal):

    def __init__(self, name):
        ## ??
        self.name = name
        print "Dog: "

## ??
class Cat(Animal):

    def __init__(self, name):
        ## ??
        self.name = name
        print "Cat: "

# ??
class Person(object):

    def __init__(self, name):
        ## ??
        self.name = name
        print "Person's name is %s" % self.name
        ## Person has a pet of some kind
        self.pet = None
        print "Person's pet is %s" % self.pet

# ??
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is the strange magic?
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary

## ??
class Fish(object):
    pass

## ??
class Salmon(Fish):
    pass

## ??
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## ??
satan = Cat("Satan")

#### ??

mary = Person("Mary")

## ??
