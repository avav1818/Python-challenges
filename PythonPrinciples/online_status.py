#!/usr/bin/env python3

# https://pythonprinciples.com/challenges/Online-status/ 

def online_count(statuses):
    counter = 0
    
    for k,v in statuses.items():
        if v == "online":
            counter += 1
    
    return counter 