#!/usr/bin/python3
class Square():
    def check_values(self, size):
        if (type(size) != int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")

    def __init__(self, size=0):
        self.check_values(size)
        self.__size = size

    @property
    def size(self):
        return(self.__size)

    @size.setter
    def size(self, size=0):
        self.check_values(size)
        self.__size = size

    def area(self):
        return(self.__size**2)
