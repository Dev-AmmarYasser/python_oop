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


Member.show_users_num()

print(member_one.full_name())
print(Member.full_name(member_one))


print('-' * 15)

Member.say_hello()

Member.hello_user('Ammar')
