# CS 122 Fall 2025 Project 3
# Author: Quinn Smiley
# Credit: ChatGPT
# Description: Provide your own description

#test = 'banana'
test = 'When in the course of human events'
def reverse(s):
    reverse_str = ''
    for ch in s:
        reverse_str = ch + reverse_str
    return reverse_str
result = reverse(test)
print(result)

"""
The reverse() function uses a for loop to reverse a string by rearranging the individual letters. 

The reverse() function takes a arguement (s), that is a string. Then, iniitalizes the reverse_str variable to contain an empty string. Then, it uses a for loop to loop through each character of the s parameter - breaking up the sting into individual letters. Within the loop, the reverse_str variable is given a value of a character plus the initial empty string. This results in a step-by-step format when it is returned:
b
ab
nab
etc. When the loop goes through every character, it returns ananab last. To ensure that only the full reversed string is printed, reverse(test) is set equal to result which will then be printed.  

Args:
   s (str): can be any string that is reversed when run through the function.

Returns:
   Reversed version of s.
"""