class Member:
    # Class Attributes => Defined outside constructor function
    good_names = ['hello']

    users_num = 0

    def __init__(self, first_name, middle_name, last_name, gender='male'):
        # Instance Attributes
        self.fname = first_name
        self.mname = middle_name
        self.lname = last_name
        self.gender = gender.lower()

        Member.users_num += 1

        # print(Member.users_num)

    @classmethod
    def show_users_num(cls):
        print(f"We have {cls.users_num} Users In Our System.")
        print(f"We have {Member.users_num} Users In Our System.")

    @staticmethod
    def say_hello():
        print('Hello from static method')

    @staticmethod
    def hello_user(user_name):
        print(f"Hello {user_name}")

    def delete_user(self):
        Member.users_num -= 1
# Instance Methods

    def full_name(self):
        if self.fname in Member.good_names:
            raise ValueError('Good')
        else:
            return f"{self.fname} {self.mname} {self.lname}"

    def name_with_title(self, title='how are you'):
        if self.gender == 'male':
            return f"Hello Mr.{self.fname} , {title}"
        else:
            return f"Hello Mrs.{self.fname} , {title}"

    def get_all_info(self):
        return f"{self.name_with_title()} , Your name is {self.full_name()}"


# print(Member.users_num)

member_one = Member("Ammar", 'Yasser', 'Elhoseiny')
member_two = Member("hello", 'Yasser', 'Elhoseiny')


# Member.show_users_num()

# print(member_one.full_name())
# print(Member.full_name(member_one))


print('-' * 15)

# Member.say_hello()

# Member.hello_user('Ammar')


class Skill:
    def __init__(self):
        self.skills = ['html', 'css', 'js']

    def __str__(self):
        return f"My skills : {self.skills}"

    def __len__(self):
        return len(self.skills)


profile = Skill()

# print(len(profile))

# profile.skills.append('python')


# print(profile)
# print(len(profile))
# print(profile.__class__)

# print('-' * 10)


# Base Class
class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        print(
            f'Instance {self.name} created from base class with price {self.price}')

    def eat(self):
        print('eat method from base class')


# Derived Class
class Apple(Food):
    def __init__(self, name, price, amount):
        # Food.__init__(self, name, price)
        super().__init__(name, price)
        self.amount = amount
        print(
            f'Instance {self.name} created from derived class with price {self.price} , amount => {self.amount}')
        # Food.eat(self)


food_two = Apple('Pizza', 150, 3)


food_two.eat()


# class Dog:
#     species = "Canis familiaris"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name} is {self.age} years old"

#     def speak(self, sound):
#         return f"{self.name} says {sound}"


# class JackRussellTerrier(Dog):

#     def speak(self, sound="Arf"):
#         return super().speak("Arf2")
#         # return f"{self.name} barks: {sound}"


# class Dachshund(Dog):
#     def __init__(self, name, age, message):
#         super().__init__(name, age)
#         self.msg = message
#         print(self.msg)

#     def speak(self, sound="How"):
#         return f"{self.name} says {sound}"


# class Bulldog(Dog):
#     pass


# miles = JackRussellTerrier("Miles", 4)
# buddy = Dachshund("Buddy", 9, "Hello World")
# jack = Bulldog("Jack", 3)
# jim = Bulldog("Jim", 5)

# print('-' * 10)

# print(miles.species)

# print(miles.name)
# print(miles.age)

# print('-' * 10)

# print(buddy.name)
# print(buddy.age)
# print(buddy.msg)

# print('-' * 10)

# print(isinstance(miles, JackRussellTerrier))

# print(isinstance(miles, Dog))

# print('-' * 10)

# print(miles.speak())

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)


dog1 = GoldenRetriever("Dog1", 4)

# print(dog1.speak())


class BaseOne:
    def __init__(self):
        print('1')

    def func_one(self):
        print('1')


class BaseTwo:
    def __init__(self):
        print('2')

    def func_two(self):
        print('2')


class Derived(BaseOne, BaseTwo):
    pass


print('-'*15)

my_var = Derived()

# print(Derived.mro())

my_var.func_one()
my_var.func_two()


class Base:
    pass


class DerivedOne(Base):
    pass


class DerivedTwo(DerivedOne):
    pass


# Polymorphism

# Abstract Base Class (ABC)
class A:
    def do_something(self):
        print('From Class A')

        raise NotImplementedError("Please Implement This Method In Your Class")


class B(A):
    def do_something(self):
        print("From Class B")


class C(A):
    def do_something(self):
        print("From Class C")


my_instance = C()

print('-'*15)

my_instance.do_something()
