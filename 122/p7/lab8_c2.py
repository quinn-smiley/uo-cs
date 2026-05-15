# CS 122 Fall 2025 Lab 8
# Author: Quinn Smiley
# Credit: ChatGPT
# Description: Lab 8 challenges

#
# Challenge functions
#

def count_lines(filename, include_empty_lines = True):
    count = 0
    fin = open(filename)
    for line in fin:
        stripped = line.strip()
        if include_empty_lines:
            count += 1
        else: 
            if stripped != "":
                count += 1
    fin.close()
    return count



#
# main() function to test your code
#
def main():
    filename = "sample1.txt"
    count = count_lines(filename)
    empty = count_lines(filename, False)
    print("File: ", filename)
    print("Total lines: ", count)
    print("Total non-empty lines: ", empty)
# Only call main() if this file is executed (not imported)
if __name__ == "__main__":
    main()