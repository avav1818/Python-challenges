#!/usr/bin/env python3

# https://pythonprinciples.com/challenges/Palindrome/ 

def palindrome(string):

    reversed_string = string[::-1]

    if string == reversed_string:
        return True
    else:
        return False 
