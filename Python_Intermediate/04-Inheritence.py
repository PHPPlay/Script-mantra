#!/usr/bin/python3

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Cat(Pet):
    def __init__(self, name, age):
        super().__init__(name, age) # You can run super class method like this

def Main():

    thePet = Pet("Pet", 1)
    jess = Cat("Jess", 3)

    print ("is jess a Cat?" + str(isinstance(jess, Cat)))
    print ("is jess a Pet?" + str(isinstance(jess, Pet)))
    print ("is ThePet a Cat? " + str(isinstance(thePet, Pet)))
    print ("is thePet a Pet" + str(isinstance(thePet, Cat)))

    print(jess.name)

if __name__ == '__main__':
    Main()


