#!/usr/bin/python3

#def hello():
#    print("hello")
#    print("hello")

#print("started")
#hello()
#hello()
#hello()

#def getInteger():
def getInteger(prompt):
    result = int(input(prompt))
    return result
def Main():
    print("started")
    output = getInteger("Please enter an integer: ")
    output_2 = getInteger("Please enter another integer: ")
    print("The first integer is " + str(output) + "\n" + "The second integer is " + str(output_2))

if __name__ == "__main__":
    Main()