#!/usr/bin/env python3

# https://pythonprinciples.com/challenges/Adding-and-removing-dots/ 

def add_dots(string):

    # Characters form the input string followed by a dot "."
    dots = [ 
        "{0}{1}".format(string[i],".")
        for i in range(len(string))
        ]

    # From the above list comprehension, a "." is placed at the end of the string
    # This final dot is not required and is sliced of below
    final_string = "".join(dots)[:-1]

    return final_string
    
def remove_dots(string):
    
    dots_removed = string.replace(".", "")
    
    return dots_removed