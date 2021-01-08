#!/usr/bin/env python3

# https://pythonprinciples.com/challenges/Anagrams/ 

def is_anagram(string1, string2):
    
    # Checking if sorted strings of equal length match. 
    if len(string1) == len(string2): 
        if sorted(string1) == sorted(string2):
            return True
        else:
            return False
    else: 
        return False 

