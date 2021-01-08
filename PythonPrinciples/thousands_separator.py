#!/usr/bin/env python3

# https://pythonprinciples.com/challenges/Thousands-separator/

# Built-in solution using string formatting 
def format_number(num):
    thousands_separated = "{:,}".format(num)
    return str(thousands_separated)

# Alternarive DIY solution
def format_number_v2(n):
    result = ""
    for i, digit in enumerate(reversed(str(n))):
        if i != 0 and (i % 3) == 0:
            result += ","
        result += digit
    return result[::-1]
