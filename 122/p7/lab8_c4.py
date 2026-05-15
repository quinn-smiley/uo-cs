# CS 122 Fall 2025 Lab 8
# Author: Quinn Smiley
# Credit: ChatGPT
# Description: Lab 8 challenges

#
# Challenge functions
#

def sum_numbers(t):
    total = 0
    for num in t:
        total += num
    return total
    

#
# main() function to test your code
#
def main():
    num_list = [6, 3, 9, 5, 11, 22, 7, 8, 2, 4]
    total = sum_numbers(num_list)
    count = len(num_list)
    if count != 0:
        average = total / count
    else:
        average = 0

    print("Numbers:", num_list)
    print("Count:", count)
    print("Sum:", total)
    print("Average:", average)

# Only call main() if this file is executed (not imported)
if __name__ == "__main__":
    main()