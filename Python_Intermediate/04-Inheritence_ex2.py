#!/usr/bin/python3

class Pet:
    def __init__(self, my_name, my_age):
        self.fuck_name = my_name
        self.fuck_age = my_age

    def talk(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Cat(Pet):
    def __init__(self, my_name, my_age):
        super().__init__(my_name, my_age)

    def talk(self):
        return "Meowww"


class Dog(Pet):
    def __init__(self, my_name, my_age):
        super().__init__(my_name, my_age)

    def talk(self):
        return "Wooff!"


def Main():
    #pets = [Cat("jess", 3), Dog("Jack", 2), Cat("fred", 7), Pet("thePet", 5)]
    pets = [Cat("jess", 3), Dog("Jack", 2), Cat("fred", 7)]
    for pet in pets:
        print("Name:" + pet.fuck_name + ", Age:" + str(pet.fuck_age) + ", says:" + pet.talk())


if __name__ == '__main__':
    Main()

