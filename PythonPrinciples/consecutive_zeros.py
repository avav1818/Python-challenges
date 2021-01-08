#!/usr/bin/env python3

# https://pythonprinciples.com/challenges/Consecutive-zeros/

def consecutive_zeros(string):
    return  max(map(len,string.split('1'))) 
