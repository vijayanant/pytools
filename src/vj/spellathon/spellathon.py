'''
Created on Jul 2, 2012

@author: Vijay Ananth
'''
import sys
import os
import argparse
from vj.tools import toolsLib



def findPossibleWords(keyAlphabet, alphabetList, dict):
    """Lists all the words that are made up of the chars in
    'alphabetList' and must contain 'keyAlphabet'"""
    with open(dict) as f:
        lines = f.read().splitlines()
        
    wordlist=[]
    for word in lines:
        if keyAlphabet in word and toolsLib.containsOnlyFrom(word, alphabetList):
            wordlist.append(word)
    return wordlist

def processArgs(args):
    dict_file=os.path.join(os.path.dirname(__file__),'sampleDictionary.dict')
    
    parser = argparse.ArgumentParser(description='Find all possible valid words using a list alphabets')
    parser.add_argument('-k', '--key', action="store", dest='key',
                        help='Alphabet that all words must contain')
    parser.add_argument('-l', '--list', action="store", dest="list",
                        help='Alphabets using which words are to be formed including key')
    parser.add_argument('-d', '--dict', action="store", dest="dict", nargs='?',
                        help='Absolute path to a dictionary file', default=dict_file)
    
    return parser.parse_args(args)
      
if __name__ == '__main__':
    args=processArgs(sys.argv[1:])
    print args
    myWordList=findPossibleWords(args.key,args.list, args.dict)
    print myWordList