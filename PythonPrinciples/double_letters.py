#!/usr/bin/env python3

# https://pythonprinciples.com/challenges/Double-letters/ 

def double_letters(string):

    for i in range(1, len(string)):

        current_index = string[i]
        preceding_index = string[i-1]     

        # Check the current index value of the string and compare it to the prior index
        if current_index == preceding_index:
            return True
    
    return False


