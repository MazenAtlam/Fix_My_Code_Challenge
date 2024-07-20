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

        self.width = width
        self.height = height

    def area_of_my_square(self):
        """
        Area of the square

        Return:
            The area of the square
        """

        return self.width * self.height

    def PermiterOfMySquare(self):
        """
        Compute the perimeter of the square

        Return: The perimeter of the square
        """

        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """
        Formating the square printing

        Return: A string to be printed
        """

        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """Creates a square instance"""

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
