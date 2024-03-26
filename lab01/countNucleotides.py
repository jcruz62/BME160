#!/usr/bin/env python3
# Name: Jade Cruz(jcruz62)
# Group Members: none

"""
create a dnaString object that will return the count of each base.

Using the input: DNA string, it will output the number of A,T,G,C 
"""

class dnaString (str):
    def length (self):
        return (len(self))

    def getAT (self):
        num_A = self.count("A")
        num_T = self.count("T")
        num_C = self.count("C")
        num_G = self.count("G")
        return ((num_A + num_T)/ self.len() )
    def countNucleotideA (self):
        num_A = self.count('A')
        return num_A
    def countNucleotideC (self):
        num_C = self.count('C')
        return num_C
    def countNucleotideG (self):
        num_G = self.count('G')
        return num_G
    def countNucleotideT (self):
        num_T = self.count('T')
        return num_T
    

dna = input("Enter a dna sequence: ")
upperDNA = dna.upper()
coolString = dnaString(upperDNA)

print("Your sequence is " + str(len(coolString)) + " nucleotides long with the following breakdown of bases:")
print ("number As = {} number Cs = {} number Gs = {} number Ts = {}".format(
    coolString.countNucleotideA(),coolString.countNucleotideC(),coolString.countNucleotideG(),coolString.countNucleotideT()) )
