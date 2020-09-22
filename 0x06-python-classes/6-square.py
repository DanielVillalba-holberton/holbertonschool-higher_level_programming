#!/usr/bin/python3


class Square:
    def __init__(self, size=0, position=(0, 0)):
        if type(size) != int:
            raise TypeError("size must be an integer")
        else:
            if size >= 0:
                self.__size = size

        self.__position = position

    def area(self):
        ar = self.__size ** 2
        return ar

    def my_print(self):
        if (self.__size == 0):
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        else:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if ((len(value) != 2) or (type(value[1] != int) or
           (type(value[2]) != int))or (value[0] < 0 or value[1] < 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
