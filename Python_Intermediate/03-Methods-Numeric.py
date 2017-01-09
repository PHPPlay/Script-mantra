#!/usr/bin/python3

import math

class Vector2D:

    def __init__(self, x, y):
        self.a = x
        self.b = y

    def __add__(self, other):
        return Vector2D(self.a + other.a, self.b + other.b)

    def __iadd__(self, other):
        self.a += other.a
        self.b += other.b
        return self

    def __sub__(self, other):
        return Vector2D(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        return Vector2D(self.a * other.a, self.b * other.b)

    def __imul__(self, other):
        self.a *= other.a
        self.b *= other.b
        return self
    def __div__(self, other):
        return Vector2D(self.a/other.a, self.b/other.b)

    def getLength(self):
        return math.sqrt(self.a**2 + self.b**2)

    def normalized(self):
        length = self.getLength()
        if length != 0:
            return Vector2D(self.a/length, self.b/length)
        return Vector2D(self)

    def getAngle(self):
        return math.degrees(math.atan2(self.b,self.a))

    def __str__(self):
        return "X: " + str(self.a) + ", Y: " + str(self.b)

def Main():
    vec = Vector2D(7,8)
    vec2 = Vector2D(2,3)
    print(vec)
    print (vec2)

    tempmethod = vec.getAngle

    vec = vec + vec2
    print(vec)

    vec += vec2
    print (vec)

    vec *= Vector2D(2,2)
    print (vec)

    print(vec.normalized())
    print(vec.getAngle())

    print(tempmethod())


if __name__ == '__main__':
    Main()