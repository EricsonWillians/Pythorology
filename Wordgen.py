"""
WordGen 1.0.
Written by Ericson Willians.
"""

import itertools as it
import Pythorology

class WordGen:

    def __init__(self, v, c):
        w = open("w.txt", "r")
        self.words = [x.replace('\n', '') for x in w.readlines()]
        self.v = v # Vowel.
        self.c = c # Consonant.
        self.decoded = [(x, pythorology.Vcipher(x).v.to_one(), pythorology.Vcipher(x).c.to_one()) for x in self.words]
    
    def _filter(self):
    
        return [x for x in self.decoded if x[1] == self.v and x[2] == self.c]
        
if __name__ == "__main__":

    v = int(raw_input("Desired number for Vowels: "))
    c = int(raw_input("Desired number for Consonants: "))

    gen = WordGen(v, c)
    print gen._filter()
