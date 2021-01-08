#!/usr/bin/env python3

# https://pythonprinciples.com/challenges/List-xor/

def list_xor(n, list1, list2):
    if (n in list1) and (n not in list2):
        return True
    elif (n in list2) and (n not in list1):
        return True
    else:
        return False 
