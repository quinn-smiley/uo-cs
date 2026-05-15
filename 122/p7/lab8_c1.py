# CS 122 Fall 2025 Lab 8
# Author: Quinn Smiley
# Credit: ChatGPT
# Description: Lab 8 challenges

#
# Challenge functions
#

def count_lines(filename):
    count = 0
    fin = open(filename)
    for line in fin:
        fin.readline()
        count += 1
    fin.close()
    return count



#
# main() function to test your code
#
def main():
    filename = "sample1.txt"
    count = count_lines("sample1.txt")
    print("File: ", filename)
    print("Total lines: ", count)
# Only call main() if this file is executed (not imported)
if __name__ == "__main__":
    main()