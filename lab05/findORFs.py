#!/usr/bin/env python3
# Name: Your Jade Cruz(jcruz62)
# Group Members: Ranvir Singh (rsingh63) and Ryan Fong (rfong8)

from sequenceAnalysis import FastAreader
import sys

'''
pseudocode: For my code I used 3 different methods which are findOrfs, boundaryConditions, and reverseStrand.


def findOrfs(self, frame, sequence, startCodon, stopCodon, orf): 
# For this method it determines the orfs in a sequence

determine frame direction
initialize start and stop positions
initialize index
i = i +3

itereate through seqeunce
while i < len(sequence) -  2:
   get codon
   
   check for startCodon
   check for stopCodon
   
   check for both stop and start codon
       calc orf position
    
    restart positions
    
move onto next codon
    
########################################################################################################
def boundaryConditions(self, frame, sequence, startCodon, stopCodon, orf):
This method handles the boundary cases such as dangling starts and stops.

determine frame direction

initilize dangling

iterate through sequence
for i from Frame - 1 to length(sequence) - 2 in steps of 3:
    get codon
    
    check if codon is in stopCodon
        if codon found and no dangling set, mark position
    
    
check if startCodon found after the dangling stop codon
    add Orf to list

return dangling and start

########################################################################################################

def reverseStrand(self, inputSeq):
This method gets the opposite of the foward strand. 

initilaize empty string for reverse bases

itererate through each base
    convert each base to its complement
    
return reverse
########################################################################################################
def main(): 
outputs the orfs

get start,stop, minGene length from commandLine arguements

initilaize orfFinder

itereate through each seq through fasta file
    generate reverse seq
    find orfs for -3,-2,-1,1,2,3
    
sort by length
filter orfs by minGene length

print orfs
'''

class CommandLine() :
    '''
    Handle the command line, usage and help requests.

    CommandLine uses argparse, now standard in 2.7 and beyond. 
    it implements a standard command line argument parser with various argument options,
    a standard usage and help.

    attributes:
    all arguments received from the commandline using .add_argument will be
    avalable within the .args attribute of object instantiated from CommandLine.
    For example, if myCommandLine is an object of the class, and requiredbool was
    set as an option using add_argument, then myCommandLine.args.requiredbool will
    name that option.
 
    '''
    
    def __init__(self, inOpts=None) :
        '''
        Implement a parser to interpret the command line argv string using argparse.
        '''
        
        import argparse
        self.parser = argparse.ArgumentParser(description = 'Program prolog - a brief description of what this thing does', 
                                             epilog = 'Program epilog - some other stuff you feel compelled to say', 
                                             add_help = True, #default is True 
                                             prefix_chars = '-', 
                                             usage = '%(prog)s [options] -option1[default] <input >output'
                                             )
        self.parser.add_argument('-lG', '--longestGene', action = 'store', nargs='?', const=True, default=False, help='longest Gene in an ORF')
        self.parser.add_argument('-mG', '--minGene', type=int, choices= (100,200,300,500,1000), default=100, action = 'store', help='minimum Gene length')
        self.parser.add_argument('-s', '--start', action = 'append', default = ['ATG'],nargs='?', 
                                 help='start Codon') #allows multiple list options
        self.parser.add_argument('-t', '--stop', action = 'append', default = ['TAG','TGA','TAA'],nargs='?', help='stop Codon') #allows multiple list options
        self.parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1')  
        if inOpts is None :
            self.args = self.parser.parse_args()
        else :
            self.args = self.parser.parse_args(inOpts)

#ENTER HERE
class OrfFinder:
    '''class with 3 methods that will help determine the orfs in a sequence'''
    
    def findOrfs(self, frame, sequence, startCodon, stopCodon, orf):
        '''determines the orfs in a dna seq'''
        
        self.boundaryConditions(frame, sequence, startCodon, stopCodon, orf)

        # Determine frames
        Frame = -frame if frame < 0 else frame

        start = -1
        stop = -1
        
        i = Frame - 1

        # Iterate through the sequence using a while loop
        while i < len(sequence) - 2:
            codon = sequence[i:i + 3]
            if codon in startCodon and start == -1:
                start = i
            if codon in stopCodon and start != -1:
                stop = i
            if start != -1 and stop != -1:
                if frame < 0:
                    orf.append((frame, len(sequence) - (stop + 2), len(sequence) - start))
                else:
                    orf.append((frame, start + 1, stop + 3))
                # Reset positions
                start = -1
                stop = -1
            i += 3

    def boundaryConditions(self, frame, sequence, startCodon, stopCodon, orf):
        '''handles boundary cases such as dangling start and stop, adds it to orf list'''
        
        # Determine the frame, same implemetation as findOrfs
        Frame = -frame if frame < 0 else frame

        danglingStop = -1
        lastStart = -1

        for i in range(Frame - 1, len(sequence) - 2, 3):
            codon = sequence[i:i + 3]

            if codon in stopCodon:
                if danglingStop == -1:
                    danglingStop = i
                    orf.append((frame, 1, danglingStop + 3))
                break

            if codon in startCodon:
                lastStart = i

        if lastStart != -1 and lastStart > danglingStop:
            orf.append((frame, lastStart + 1, len(sequence)))

        return danglingStop, lastStart
            
    
    def reverseStrand(self, inputSeq):
        '''returns the reverse strand of the forward sequence'''
        reverse = ""
        for base in inputSeq[::-1]:
            if base == "A":
                reverse += "T"
            elif base == "T":
                reverse += "A"
            elif base == "C":
                reverse += "G"
            elif base == "G":
                reverse += "C"
        return reverse
    
def main(inFile = None, options = None):
    '''
    format and output orfs
    '''
    thisCommandLine = CommandLine(options)
    reader = FastAreader(inFile)
    
    readFile = reader.readFasta()
    
    startCodon = thisCommandLine.args.start
    stopCodon = thisCommandLine.args.stop
    minGene = thisCommandLine.args.minGene
    
    orfFinder = OrfFinder()
    
    for header, sequence in readFile:
        reverse = orfFinder.reverseStrand(sequence)
        
        orf = []
        orfFinder.findOrfs(1, sequence, startCodon, stopCodon, orf)
        orfFinder.findOrfs(2, sequence, startCodon, stopCodon, orf)
        orfFinder.findOrfs(3, sequence, startCodon, stopCodon, orf)
        orfFinder.findOrfs(-1, reverse, startCodon, stopCodon, orf)
        orfFinder.findOrfs(-2, reverse, startCodon, stopCodon, orf)
        orfFinder.findOrfs(-3, reverse, startCodon, stopCodon, orf)
        
        print(header)
        
        # sorting by length
        orf.sort(key = lambda x: (x[2] - x[1], -x[1]), reverse = True)
        orf = list(filter(lambda x: (x[2] - x[1] + 1) >= minGene, orf))

        
        for eachOrf in orf:
            frame = eachOrf[0]
            start = eachOrf[1]
            end = eachOrf[2]
            length = eachOrf[2] - eachOrf[1] + 1
            sys.stdout.write('{:+d} {:>5d}..{:>5d} {:>5d}\n'.format(frame, start, end, length))
        
    

if __name__ == "__main__":
    main(inFile = 'tass2.fa', options = ['-mG=300', '-lG']) # delete this stuff if running from commandline
