#!/usr/bin/python3

import math

def Main():
    try:
        number = float(input("Please enter a number: "))
        number = math.fabs(number)
        print(number)

    except:
        print("You did not enter a number")



if __name__ == '__main__':
    Main()
