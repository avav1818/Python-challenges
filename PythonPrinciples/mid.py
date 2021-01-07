#!/usr/bin/env python3

# https://pythonprinciples.com/challenges/Middle-letter/ 

def mid(string):
   # Strings of an even length have no mid point.
    if len(string) % 2 == 0:
       return ""
    else:
        midpoint = len(string) // 2
        return string[midpoint]
