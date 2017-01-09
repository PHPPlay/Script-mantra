#!/usr/bin/python3

import math

def Main():
    try:
        radius = float(input("Please enter a radius: "))
        area = math.pi * radius**2
        print("area = ", area)
    except:
        print("Please enter the correct radius value: ")



if __name__ == '__main__':
    Main()