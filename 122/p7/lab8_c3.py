# CS 122 Fall 2025 Lab 8
# Author: Quinn Smiley
# Credit: ChatGPT
# Description: Lab 8 challenges

#
# Challenge functions
#

def sum_integers(filename):
    total = 0
    fin = open(filename)
    for line in fin:
        stripped = line.strip()
        if len(stripped) != 0:
            if stripped[0] != "#":
                total += int(stripped)
    fin.close()
    return total



#
# main() function to test your code
#
def main():
    filename = "sample2.txt"
    sum_int = sum_integers(filename)
    print("File: ", filename)
    print("Total: ", sum_int)
# Only call main() if this file is executed (not imported)
if __name__ == "__main__":
    main()