#!/usr/bin/env python3
x = int(input("Enter your age: "))
class age_classifier:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        return f"{self.name}! You are {self.age} yrs old\n Thanks for trusting us"

usr_ = age_classifier('Alvine', x)
print(usr_.info())
