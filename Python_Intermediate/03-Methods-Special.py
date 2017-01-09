#!/usr/bin/python3

class Vector2D:
    def __init__(self, x, y):
        self.a = x
        self.b = y


def Main():
    vec = Vector2D(5, 6)
    print("X: " + str(vec.a) + ",Y: " + str(vec.b))


if __name__ == '__main__':
    Main()
