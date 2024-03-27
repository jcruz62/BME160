#!/usr/bin/env python3
# Name: Jade Cruz(jcruz62)
# Group Members: Ryan Fong (rfong8), Ranvir Singh (rsingh63)

import sys
class FastAreader :
    
    def __init__ (self, fname=''):
        '''contructor: saves attribute fname '''
        self.fname = fname
            
    def doOpen (self):
        if self.fname == '':
            return sys.stdin
        else:
            return open(self.fname)
        
    def readFasta (self):
        
        header = ''
        sequence = ''
        
        with self.doOpen() as fileH:
            
            header = ''
            sequence = ''
            
            # skip to first fasta header
            line = fileH.readline()
            while not line.startswith('>') :
                if not line: # we are at EOF
                    return header, sequence
                line = fileH.readline()
            header = line[1:].rstrip()

            for line in fileH:
                if line.startswith ('>'):
                    yield header,sequence
                    header = line[1:].rstrip()
                    sequence = ''
                else :
                    sequence += ''.join(line.rstrip().split()).upper()

        yield header,sequence

########################################################################
# Main
# Here is the main program
# 
########################################################################
class FindUnique:
    def __init__(self, header, sequence):
        '''initialize and remove unwanted characters (this is much easier than making another method)'''
        # remove spaces from header
        self.header = header.replace(" ","")
        # # remove allignment characters (".","_","-")
        self.sequence = sequence.replace(".", "").replace("-","").replace("_","")

        powerset = self.getAllSubstrings(sequence)
        self.powerset = powerset

    def getHeader(self):
        '''returns header'''
        return self.header
    
    def getSequence(self):
        '''returns sequence'''
        return self.sequence

    def removeUnion(self, others):
        '''removes union of other sets from current sets'''
        unionOther = set()
        for other in others:
            if self == other:
                continue
            unionOther = unionOther.union(other.powerset)
            
            
        # remove union of other sets from current
        self.powerset = self.powerset.difference(unionOther)

    def keepMinimalSubstrings(self):
        '''determines the minimal substrings'''
        remove = set()
        for i in self.powerset:
            for j in self.powerset:
                if i == j: 
                    continue
                if i in j: 
                    remove.add(j)
        self.powerset.difference_update(remove)

    def getAllSubstrings(self, s):
        '''determine substrings'''
        substrings = set()
        for start in range(len(s)):
            for end in range(start + 1, len(s) + 1):
                substrings.add(s[start:end])
        return substrings

def main():
    '''output and sorts by number of .'''
    reader = FastAreader()
    reader = FastAreader('bos-tRNA-7.fa')
    #reader = FastAreader("bos-tRNA.fa")
    read = reader.readFasta()

    reads = []
    
    for header, sequence in read:
        new = FindUnique(header, sequence)
        reads.append(new)

    reads.sort(key=lambda x: (x.header))
    
    for read in reads:
        read.removeUnion(reads)
        read.keepMinimalSubstrings()
        seq = read.getSequence()
        
        
        # we need to convert powerset list to list for indexing
        powersetList = list(read.powerset)
        
        # this is what we want to output
        outputList = []
        
        # for each rna in powersetList
        for k in powersetList:
            # where substrings are found 
            # use .startswith method, return true when (k,i) true
            found = [i for i in range(len(seq)) if seq.startswith(k, i)]
            for j in found:
                modified = "." * j + k
                outputList.append(modified)
        
        # we need to sort by .
        outputList.sort(key=lambda x: x.count("."))
        
        # format
        out_str = f"{read.getHeader()}\n{read.getSequence()}\n"
        for modified_rna in outputList:
            out_str += f"{modified_rna}\n"
        
        # to stdout
        sys.stdout.write(out_str)


if __name__ == "__main__":
    main()  
