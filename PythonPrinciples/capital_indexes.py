#!/usr/bin/env python3

# https://pythonprinciples.com/challenges/Capital-indexes/

def capital_indexes(string):
    cap_indexes = [i for i in range(len(string)) if string[i].isupper()]
    return cap_indexes