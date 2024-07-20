#!/usr/bin/python3
"""A module for User class"""


class User():
    """User class"""

    def __init__(self):
        """Initialize attributes"""

        self.__email = None

    @property
    def email(self):
        """
        A property of the private attribute email

        - If the email passed is not a string, a TypeError will be raised

        Returns:
            The user email
        """

        return self.__email

    @email.setter
    def email(self, value):
        if type(value) is not str:
            raise TypeError("email must be a string")

        self.__email = value


if __name__ == "__main__":

    u = User()
    u.email = "john@snow.com"
    print(u.email)
