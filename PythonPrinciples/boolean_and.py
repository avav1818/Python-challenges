#!/usr/bin/env python3

# https://pythonprinciples.com/challenges/Boolean-and/

def triple_and(p1, p2, p3):
    if (p1 == True) and (p2 == True) and (p3 == True):
        return True
    else:
        return False

# Alternative solution
def triple_and_v2(p1, p2, p3):
    return p1 and p2 and p3 