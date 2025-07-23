from abc import ABCMeta, abstractmethod
import math


class Programming(metaclass=ABCMeta):
    @abstractmethod
    def has_oop(self):
        pass


class Python(Programming):
    def has_oop(self):
        return "Hello"


one = Python()


class Animal(metaclass=ABCMeta):
    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        print("Woof!")


class Cat(Animal):
    def make_sound(self):
        print("Meow!")


cat1 = Cat()
dog1 = Dog()

cat1.make_sound()
dog1.make_sound()


class Shape(metaclass=ABCMeta):
    @property
    @abstractmethod
    def name(self):
        """Each shape must have a name"""
        pass

    @abstractmethod
    def area(self):
        """Each shape must have an area"""
        pass


class Circle(Shape):

    def __init__(self, rad):
        self.rad = rad

    @property
    def name(self):
        return "Circle"

    def area(self):
        return 3.14 * math.pow(self.rad, 2)


class Square(Shape):

    def __init__(self, side):
        self.side = side

    @property
    def name(self):
        return "Square"

    def area(self):
        return math.pow(self.side, 2)


my_circle = Circle(5)
my_square = Square(5)

print(my_circle.name)
print(my_square.name)

print(my_circle.area())
print(my_square.area())

print("-" * 40)


class Vehicle(metaclass=ABCMeta):
    @property
    @abstractmethod
    def wheels(self):
        """Each vehicle must have wheels property"""
        pass

    @abstractmethod
    def start_engine(self):
        """Each vehicle must have method that starts its engine"""
        pass


class Car(Vehicle):
    @property
    def wheels(self):
        return "Car has 4 wheels"

    def start_engine(self):
        print("Starting car engine...")


my_car = Car()

print(my_car.wheels)

my_car.start_engine()


try:
    my_vehicle = Vehicle()
except TypeError as e:
    print(f"Error : {e}")


class DataProcessor(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def load_data():
        pass

    @staticmethod
    @abstractmethod
    def process_data():
        pass

    @staticmethod
    @abstractmethod
    def save_data():
        pass


class CSVProcessor(DataProcessor):
    @staticmethod
    def load_data():
        print("Loading data...")

    @staticmethod
    def process_data():
        print("Processing data...")

    @staticmethod
    def save_data():
        print("Saving data...")


my_csv_processor = CSVProcessor()

my_csv_processor.load_data()
my_csv_processor.process_data()
my_csv_processor.save_data()
