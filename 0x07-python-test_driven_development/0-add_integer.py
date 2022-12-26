#!/usr/bin/python3
def add_integer(a, b=98):
        if type(a) is not int and type(a) is not float:
            raise TypeError('a must be an integer')
        if type(b) is not int and type(a) is not float:
            raise TypeError('b must be an integer')
            return int(a) + int(b)
print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
print(add_integer(4, "School"))
