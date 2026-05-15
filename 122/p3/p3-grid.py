# CS 122 Fall 2025 Project 3
# Author: Quinn Smiley
# Credit: ChatGPT
# Description: Provide your own description

def draw_grid(n):
    for row in range(n):
        line = ''
        for col in range(1, n + 1):
             line = line + str(col) + ' '
        print(line)    
        
draw_grid(3)

"""
The draw_grid() function uses multiple loops to create a grid separated by rows and columns

The draw_grid() function takes the parameter n which is an integer. Then it uses a for loop cycle through the rows within the range of n. Within this loop line is initialized to an empty string and another loop cycles through the columns within the range from 1 to n + 1. hen, line is given the value of itself plus column (converted to a string) plus a space. Thus, creating the format for the rest of the table. 

Args:
   n (int): can be any integer. 

Returns:
   A grid with n amount of rows and columns.
"""