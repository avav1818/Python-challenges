#!/usr/bin/env python3

# https://pythonprinciples.com/challenges/Type-check/ 

def only_ints(v1, v2):
    if (type (v1) == int ) and (type (v2) == int):
        return True
    else:
        return False 