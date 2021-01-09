#!/usr/bin/env python3

# https://pythonprinciples.com/challenges/Tic-tac-toe-input/

def get_row_col(string):
    input_column = string[0]
    input_row = string[1]

    
    # Columns and rows with their associatead indexes as key value pairs
    column_row_indexes = { 
        "A" : 0, "B" : 1, "C" : 2,        
        "1" : 0, "2" : 1, "3" : 2
    }

    for col_key, col_item in column_row_indexes.items():
        for row_key, row_item in column_row_indexes.items():
            # Check to see if keys match "input_column" and "input_row"
            if (col_key == input_column) and (row_key == input_row):
                return (row_item, col_item) 

# Initial "not so pretty" solution
def get_row_col(string):
    column_command = string[0]
    row_command = string[1]

    # Key value pair of row numbers and corresponding index value on tic-tac-toe board 
    row_indexes = { "1" : 0, "2" : 1, "3" : 2}
    # Key value pair of columns letter and corresponding index value on tic-tac-toe board
    column_indexes = { "A" : 0, "B" : 1, "C" : 2}
    
     # Stores coordinates on the board as tuple values
    board_coordinates = ()
    
    for key in row_indexes:
        for key2 in column_indexes:
            if key == row_command:
                if key2 == column_command:
                    board_coordinates = board_coordinates + (row_indexes[row_command], column_indexes[column_command])
                    return board_coordinates