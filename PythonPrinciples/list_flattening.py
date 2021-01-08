#!/usr/bin/env python3

# https://pythonprinciples.com/challenges/Flatten-a-list/ 

def flatten(milutidimensional_list):
    
    flattened_list = []

    for element in milutidimensional_list:
        # Append elements from nested list 
        if isinstance(element, list):
            for elem in element:
                flattened_list.append(elem)
        else:
            # Append indiviual elements within the outer list 
            flattened_list.append(element)
            
    return flattened_list

