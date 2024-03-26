#!/usr/bin/env python3
# Name: Jade Cruz
# Group Members: none

"""
Build a Person object and have it introduce itself.

input: a string of arbitrary length, which is used to name the new person object
output: greeting printed to screen
"""

class Person:
# create a person class with attributes name and pet
    def __init__(self,name,pet):
        self.myName = name
        self.myPet  = pet
        
    def introduce (self):
        print ("Hi there, I am {0}, and i like {1}s".format(self.myName,self.myPet))


# put your new code here.
name = input("What is your name?: ") # asks user for their name, assign their input into name 
pet = input("What is your favorite pet?: ") # asks user for their favorite pet, assign their input into pet
newPerson = Person(name, pet) 
newPerson.introduce()
