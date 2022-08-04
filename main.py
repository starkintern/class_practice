# Python Object-Oriented Programming

# Data and Functions are considered attributes and methods inside classes

# Using classes as blueprints to be used more than once

# Classes are blueprints that are for making instances of that class

# Init (inserted at beginning of first function inside of class),
# and self (an argument used by functions inside classes) automate
# and take away the process of manually entering user data

# Methods == Functions, make it once, call it over and over,
# remember you need (), else it will call a variable

class Overton:

    def __init__(self, first, age, career, help):
        self.first = first
        self.age = age
        self.career = career
        self.help = help

    def job(self):
        return f"Name: {self.first}. Employment: {self.career}"

    def helps_out(self):
        return f"{self.first} helps out by {self.help}."


overton_1 = Overton("Scot", "52", "Harris Teeter", "trimming tress")
overton_2 = Overton("Melissa", "36", "SalesForce", "encouraging good behaviors")
overton_3 = Overton("Jacob", "26", "Hunting", "mowing the lawn and vacuuming the house")
overton_4 = Overton("Ella", "6", "Big sister", "putting her plate in the sink and cleaning up her toys")
overton_5 = Overton("Emily", "3", "Big sister", "putting her plate in the sink and cleaning up her toys")
overton_6 = Overton("Parky", "0.11", "Learning to walk", "smiling and lifting our spirits")

print(overton_1.job())
print(overton_2.job())

print(overton_3.helps_out())
print(overton_6.helps_out())
