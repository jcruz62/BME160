#!/usr/bin/env python3
# Name: Jade Cruz(jcruz62)
# Group Members: none

"""
Print out the most common statement in computer programming, Hello World.
""" 

''' this is a single line docstring '''
class Announcer (str): # Announcer is now defined as a kind of python string.
    def printMe (self): # creates a function printMe 
        print (self)

student = Announcer ('Hello Jade')
dog = Announcer ('bark bark')
student.printMe()
dog.printMe()
