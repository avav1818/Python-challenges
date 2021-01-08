#!/usr/bin/env python3

# https://pythonprinciples.com/challenges/Counting-syllables/ 


def count(string):
    new_list = string.split("-")
    return len(new_list)

# Alternative solution
def count_v2(string):
    number_hyphens = [i for i in range(len(string)) if string[i] == "-"]
    syllables = len(number_hyphens) + 1
    return syllables

