# Python Object-Oriented Programming

# Data and Functions are considered attributes and methods inside classes

# Using classes as blueprints to be used more than once

# Classes are blueprints that are for making instances of that class

# Init (inserted at beginning of first function inside of class),
# and self (an argument used by functions inside classes) automate
# and take away the process of manually entering user data

# Methods == Functions, make it once, call it over and over,
# remember you need (), else it will call a variable


if __name__ == "__main__":
    class Robot:

        # This is a constructor
        def __init__(self, name, color, weight):
            self.name = name
            self.color = color
            self.weight = weight

        def introduce_self(self):
            print(f"My name is {self.name}.")

    # Created new robot objects
    r1 = Robot("Tom", "red", 30)
    r2 = Robot("Jerry", "blue", 40)

    # Called introduce_self function on r1
    r1.introduce_self()
    r2.introduce_self()

    class Person:
        def __init__(self, n, p, i):
            self.name = n
            self.personality = p
            self.is_sitting = i

        def sit_down(self):
            self.is_sitting = True

        def stand_up(self):
            self.is_sitting = False

    p1 = Person("Alice", "aggressive", False)
    p2 = Person ("Becky", "talkative", True)

    # p1 owns r2
    p1.robot_owned = r2
    p2.robot_owned = r1

    p1.robot_owned.introduce_self()
