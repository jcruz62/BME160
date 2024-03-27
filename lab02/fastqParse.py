#!/usr/bin/env python3 
# Name: Jade Cruz(jcruz62)
# Group Members: None

'''
Read a FASTQ sequence line and return the insturment, Run ID, Flow Cell ID, Flow Cell Lane, Tile Number, X-coord, and Y-coord
'''

class FastqString (str):
    ''' Class docstring goes here.'''
    def parse(self):
        ''' Parse the FASTQ sequence and '''
        # start fastq seq after @
        newSeq = self[1:]
        # split at every occurance of :, which will give the seven fields needed
        fields = self.split(":")
        # display parsed fields from the FASTQ sequence
        print("Insturment =",fields[0])
        print("Run ID =",fields[1])
        print("Flow Cell ID =",fields[2])
        print("Flow Cell Lane =",fields[3])
        print("Tile Number =",fields[4])
        print("X-coord =",fields[5])
        print("Y-coord =",fields[6])
    
def main():
    ''' Enter FASTQ sequence and parse'''
    fastqSeq = input("FASTQ Sequence: ")
    fastqstring = FastqString(fastqSeq)
    parsed = fastqstring.parse() 
    
main()
