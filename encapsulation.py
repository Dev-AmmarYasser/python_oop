import math


class Member:
    def __init__(self, name, balance, password):
        self.name = name  # public
        self._balance = balance  # protected => Convention
        self.__password = password  # private

    def get_balance(self):
        print(self._balance)

    def get_password(self):
        print(self.__password)


class MyClass(Member):
    def get_my_password(self):
        print(self.__password)


one = Member("Ammar", 1200, "myPassword")

print(one.name)

one.name = "Doro"

print(one.name)

one.get_balance()

one.get_password()

# Private Attributes Can Be Accessed
print(one._Member__password)

two = MyClass("Ammar", 1200, "myPassword")

# print(two._MyClass__password)


class MyFirstClass:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name


three = MyFirstClass("Ammar")

print(three.get_name())

three.set_name("Doro")

print(three.get_name())

print(three._MyFirstClass__name)


class MySecondClass:
    def __init__(self, name):
        self.__name = name

    @property
    def my_name(self):
        return self.__name

    @my_name.setter
    def my_name(self, new_name):
        self.__name = new_name


print('-' * 20)

four = MySecondClass("Ammar")

four.my_name = "Hello"

print(four.my_name)


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * math.pow(self.radius, 2)


c = Circle(10)
print(c.area)


class User:
    def __init__(self, username, email):
        self.username = username

        if email.find('@') == -1:

            raise ValueError

        self._email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        if new_email.find("@") == -1:
            raise ValueError

        self._email = new_email


u = User("ammar", "ammar@gmail.com")
# u.email = "invalid"  # Should raise ValueError


class Rectangle:
    def __init__(self, width, length):
        if width < 0:
            raise ValueError
        self._width = width
        if length < 0:
            raise ValueError
        self._length = length

    def set_width(self, new_width):
        if new_width < 0:
            raise ValueError
        self._width = new_width

    def set_length(self, new_length):
        if new_length < 0:
            raise ValueError
        self._length = new_length

    @property
    def area(self):
        return self._width * self._length

    @property
    def perimeter(self):
        return (self._width + self._length) * 2


my_rectangle = Rectangle(5, 2)

print(my_rectangle.area)
print(my_rectangle.perimeter)

my_rectangle.set_width(3)

print("-" * 40)

print(my_rectangle.area)
print(my_rectangle.perimeter)
