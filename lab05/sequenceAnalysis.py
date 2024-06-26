class NucParams:
    rnaCodonTable = {
    # RNA codon table
    # U
    'UUU': 'F', 'UCU': 'S', 'UAU': 'Y', 'UGU': 'C',  # UxU
    'UUC': 'F', 'UCC': 'S', 'UAC': 'Y', 'UGC': 'C',  # UxC
    'UUA': 'L', 'UCA': 'S', 'UAA': '-', 'UGA': '-',  # UxA
    'UUG': 'L', 'UCG': 'S', 'UAG': '-', 'UGG': 'W',  # UxG
    # C
    'CUU': 'L', 'CCU': 'P', 'CAU': 'H', 'CGU': 'R',  # CxU
    'CUC': 'L', 'CCC': 'P', 'CAC': 'H', 'CGC': 'R',  # CxC
    'CUA': 'L', 'CCA': 'P', 'CAA': 'Q', 'CGA': 'R',  # CxA
    'CUG': 'L', 'CCG': 'P', 'CAG': 'Q', 'CGG': 'R',  # CxG
    # A
    'AUU': 'I', 'ACU': 'T', 'AAU': 'N', 'AGU': 'S',  # AxU
    'AUC': 'I', 'ACC': 'T', 'AAC': 'N', 'AGC': 'S',  # AxC
    'AUA': 'I', 'ACA': 'T', 'AAA': 'K', 'AGA': 'R',  # AxA
    'AUG': 'M', 'ACG': 'T', 'AAG': 'K', 'AGG': 'R',  # AxG
    # G
    'GUU': 'V', 'GCU': 'A', 'GAU': 'D', 'GGU': 'G',  # GxU
    'GUC': 'V', 'GCC': 'A', 'GAC': 'D', 'GGC': 'G',  # GxC
    'GUA': 'V', 'GCA': 'A', 'GAA': 'E', 'GGA': 'G',  # GxA
    'GUG': 'V', 'GCG': 'A', 'GAG': 'E', 'GGG': 'G'  # GxG
    }
    
    dnaCodonTable = {key.replace('U','T'):value for key, value in rnaCodonTable.items()}
    # dict for valid bases
    bases = {"A", "C", "T", "G", "U", "N"}

    def __init__ (self, inString=''):
        # initialize dict to store counts for later
        self.aaComp = {}
        self.nucComp = {}
        self.codonComp = {}
        
        # codon composition
        self.codonComp = {}
        for key in self.rnaCodonTable:
            self.codonComp[key] = 0;
        # get codon of length of 3
        for i in range(0, len(inString), 3):
            codon = inString[i : i+3].replace('T','U')
            self.codonComp[codon] += 1
        
       

        
    def addSequence (self, inSeq):
        '''accepts new sequences'''
        inSeq = inSeq.replace('T', 'U')
        
        # nucleotide composition count
        for nuc in inSeq:
            if nuc in self.bases:
                self.nucComp[nuc] = self.nucComp.get(nuc, 0) + 1
                
        # check if codon is in rna table, if yes then update count
        for i in range(0, len(inSeq), 3):
            codon = inSeq[i:i+3]
            if codon in self.rnaCodonTable:
                self.codonComp[codon] = self.codonComp.get(codon, 0) + 1
        
        # aa comp count
        self.aaComp = {}
        for codon in self.codonComp:
            aa = self.rnaCodonTable[codon]
            codonCount = self.codonComp[codon]
            if aa not in self.aaComp:
                self.aaComp[aa] = codonCount
            else:
                self.aaComp[aa] += codonCount
        
                
        # need to include bc above code does not accomodate for stop codons.
        # stop codons are - and does not have a length of 3
        for stopCodon in ['UAA', 'UAG', 'UGA']:
            self.codonComp.setdefault(stopCodon, 0)
            
    def aaComposition(self):
        '''return a dictionary of counts over the 20 aa and stop codons'''
        return self.aaComp


            
    
    def nucComposition(self):
        '''returns a dict of counts of valid nuc found in analysis'''
        result = {}
        for nuc in self.bases:
            result[nuc] = self.nucComp.get(nuc, 0)
            
        return result
            
    
    def codonComposition(self, inString = ''):
        '''returns the counts of codons'''
        return self.codonComp
    
    def nucCount(self):
        '''summing every valid nuc found'''
        
        total = 0
        for key, value in self.nucComp.items():
            if key in self.bases:
                total += value
        
        return total
 
import sys
class FastAreader :
    ''' 
    Define objects to read FastA files.
    
    instantiation: 
    thisReader = FastAreader ('testTiny.fa')
    usage:
    for head, seq in thisReader.readFasta():
        print (head,seq)
    '''
    def __init__ (self, fname=None):
        '''contructor: saves attribute fname '''
        self.fname = fname
            
    def doOpen (self):
        ''' Handle file opens, allowing STDIN.'''
        if self.fname is None:
            return sys.stdin
        else:
            return open(self.fname)
        
    def readFasta (self):
        ''' Read an entire FastA record and return the sequence header/sequence'''
        header = ''
        sequence = ''
        
        with self.doOpen() as fileH:
            
            header = ''
            sequence = ''
            
            # skip to first fasta header
            line = fileH.readline()
            while not line.startswith('>') :
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

            
                
    def nucCount(self):
        '''summing every valid nuc found'''
        
        total = 0
        for key, value in self.nucComp.items():
            if key in self.bases:
                total += value
        
        return total
