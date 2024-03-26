#!/usr/bin/env python3
# Name: Jade Cruz(jcruz62)
# Group Members: none

""" 
create an object dnaString that will represent a DNA sequence.


By using the input(AAAATGAATGGCTAACTTTTGAA),
the output will give us the proportion of A and T nucleotides in a DNA string
"""

class dnaString (str):
    def length (self):
        return len(self)

    def getAT (self):
        num_A = self.count("A")
        num_T = self.count("T")
        return ((num_A + num_T)/ self.length() )

dna = input("Enter a dna sequence: ")
upperDNA = dna.upper()
coolString = dnaString(upperDNA)

print ("AT content = {0:0.3f}".format(coolString.getAT()) )
