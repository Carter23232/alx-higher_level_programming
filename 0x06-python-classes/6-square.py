#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """
    class of Square
    """

    def __init__(self, size=0, position=(0, 0)):
        """constructor for initializing the instance variable
        :@size = size(private) to use
        :@position = position (private) to use
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if type(position) is not tuple or len(position) != 2 or \
                type(position[0]) is not int or \
                type(position[1]) is not int or \
                position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        """
        area of a square
        :returns square
        """
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2 or \
                type(value[0]) is not int or \
                type(value[1]) is not int or \
                value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
