# CS 122 Fall 2025 Lab 8
# Author: Quinn Smiley
# Credit: ChatGPT
# Description: Lab 8 challenges

#
# Challenge functions
#

def title_case(sentence):
    empty_list = []
    word = sentence.split(" ")
    for w in word:
        if len(w) > 0:
            first = w[0].upper()
            rest = w[1:].lower()
            new = first + rest
            empty_list.append(new)
    result = " ".join(empty_list)
    return result
        
            

#
# main() function to test your code
#
def main():
    sentence = "enjoY THE journeY!"
    title = title_case(sentence)
    print("Original: ", sentence)
    print("Title Case: ", title)

# Only call main() if this file is executed (not imported)
if __name__ == "__main__":
    main()