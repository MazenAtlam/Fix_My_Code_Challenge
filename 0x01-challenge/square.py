#!/usr/bin/python3
"""A module has a Square class"""


class Square():
    """
    A class that creates a square

    Attributes:
        width: The wigth of the square
        height: The height of the square
    """

    def __init__(self, width=0, height=0):
        """
        Initialize attributes

        Args:
            width: The wigth of the square
            height: The height of the square
        """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """A getter to the private attribute width"""

        return self.__width

    @width.setter
    def width(self, width):
        if width < 0:
            self.__width = 0
        else:
            self.__width = width

    @property
    def height(self):
        """A getter to the private attribute height"""

        return self.__height

    @height.setter
    def height(self, height):
        if height < 0:
            self.__height = 0
        else:
            self.__height = height

    def area_of_my_square(self):
        """
        Area of the square

        Return:
            The area of the square
        """

        return self.__width * self.__height

    def PermiterOfMySquare(self):
        """
        Compute the perimeter of the square

        Return: The perimeter of the square
        """

        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        Formating the square printing

        Return: A string to be printed
        """

        return "{}/{}".format(self.__width, self.__height)


if __name__ == "__main__":
    """Creates a square instance"""

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
