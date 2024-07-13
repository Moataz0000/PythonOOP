
# property decorator is change the method to properete

class Member:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def say_hello(self):
        return f'Hello {self.name}'

    @property
    def change_age_to_days(self):
        return self.age * 365


obj = Member('Mezo', 21)

print(obj.change_age_to_days)