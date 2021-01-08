#!/usr/bin/env python3

# https://pythonprinciples.com/challenges/All-equal/
 
def all_equal(values):
    values_set = set(values)

    if (len(values_set) == 0) or (len(values_set) == 1):
        return True 
    else:
        return False 

