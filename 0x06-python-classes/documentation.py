#!/usr/bin/python3
Square = __import__('5-square').Square

my_square = Square(50)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 5
print("Area: {} for size: {}".format(my_square.area(), my_square.size))


my_square.my_print()
