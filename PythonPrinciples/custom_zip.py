#!/usr/bin/env python3

# https://pythonprinciples.com/challenges/Custom-zip/

def zap(list1, list2):

    zapping = [
        (list1[i], list2[i])
        for i in range(len(list1))
    ]

    return zapping
