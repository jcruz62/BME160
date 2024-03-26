#!/usr/bin/env python3
# Name: Jade Cruz(jcruz62)
# Group Members: none

"""
Build a Person object and have it introduce itself.

input: a string of arbitrary length, which is used to name the new person object
output: greeting printed to screen
"""

class Person:
    """ Build a new Person objects with all of hte attributes given at instantiation time. """
    def __init__(self,name, username, studentType, major, reason, problem, priorExperience):
        """ Save all of the instance arguments. """
        self.myName = name
        self.username = username
        self.studentType = studentType
        self.major = major
        self.reason = reason
        self.problem = problem
        self.priorExperience = priorExperience


    def introduce (self):
        ''' Print the introductionusing all of the object atributes '''
        print ("My name is {0}".format(self.myName))
        print ("My username is {0}".format(self.username))
        print ("I am an {0}".format(self.studentType))
        print ("My major is {0}".format(self.major))
        print ("I'm taking this class because {0}".format(self.reason))
        print ("A problem I am most interested in is {0}".format(self.problem))
        print ("Prior Experience: {0}".format(self.priorExperience))
        


Jade = Person ('Jade Cruz.', 'jcruz62.', 'undergraduate.', 'BME.', "it is a major prerequisite and am interested in learning how biology and programming correlate.", 'how to handle complex data sets.', 'none.')
Jade.introduce()
