#!/usr/bin/python3
Square = __import__('3-square').Square

square_1 = Square(3)
print("Area: {}".format(square_1.area()))

try:
    print(square_1.size)
except Exception as e:
    print(e)

try:
    print(square_1.__size)
except Exception as e:
    print(e)

square_2 = Square(5)
print("Area: {}".format(square_2.area()))
