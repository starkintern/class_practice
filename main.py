# Python Object-Oriented Programming

# Data and Functions are considered attributes and methods inside classes

# Using classes as blueprints to be used more than once

# Classes are blueprints are for making instances of a class

# Init and self automate and take away the process of manually entering user data

# Methods == Functions, make it once, call it over and over

class Overton:

    def __init__(self, first, age, career):
        self.first = first
        self.age = age
        self.career = career

    def job(self):
        return f'Name: {self.first}. Employment: {self.career}'


overton_1 = Overton('Scot', '52', 'Harris Teeter')
overton_2 = Overton('Melissa', "36", 'SalesForce')
overton_3 = Overton('Jacob', '26', 'Hunting')
overton_4 = Overton('Ella', '6', 'Big sister')
overton_5 = Overton('Emily', '3', 'Big sister')
overton_6 = Overton('Parky', '0.10', 'Learning to walk')

print(overton_1.job())
print(overton_2.job())
