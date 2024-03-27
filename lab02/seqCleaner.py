#!/usr/bin/env python3 
# Name: Jade Cruz(jcruz62)
# Group Members: None

'''
Read a DNA string from user input and return a collapsed substring of embedded Ns to: {count}.

Example: 
 input: AaNNNNNNGTC
output: AA{6}GTC

Any lower case letters are converted to uppercase
'''

class DNAstring (str):
  def length (self):
    return (length(self))
  def purify(self):
    ''' Return an upcased version of the string, collapsing a single run of Ns.'''
    pureDNA = self.upper()
    # count the number of N's
    countN = self.count("N")
    # replace N's with ""
    pureDNA = self.replace("N", "")
    # find the first occurance of N
    findN = self.find("N")
    # foramt pureDNA to look like (bases before N then {countN} then rest of bases)
    pureDNA = pureDNA[:findN] + "{"+ str(countN) +"}" + pureDNA[findN:]
    return pureDNA
      
def main():
  ''' Get user DNA data and clean it up.'''
  data = input('DNA data?')
  while (data):
    thisDNA = DNAstring (data)
    pureData = thisDNA.purify()
    print (pureData)
    data = input('DNA data?')
    
main()
