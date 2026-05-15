# CS 122 Fall 2025 Lab 8
# Author: Quinn Smiley
# Credit: ChatGPT
# Description: Lab 8 challenges

#
# Challenge functions
#

from lab8_c5 import title_case

def remove_vowels(words):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    results = []
    for word in words: 
        empty = ""
        for ch in word: 
            if ch not in vowels: 
                empty = empty + ch
        results.append(empty)
    return results
    


#
# main() function to test your code
#
def main():
    sentence = input("Enter sentence: ")
    words = sentence.split()
    sorted_words = sorted(words)
    vowels_removed = remove_vowels(words)
    vowels_join = " ".join(vowels_removed)
    title_version = title_case(sentence)
    print("Original sentence:", sentence)
    print("Sorted words:", sorted_words)
    print("Vowels removed:", vowels_join)
    print("Title case sentence:", title_version)

# Only call main() if this file is executed (not imported)
if __name__ == "__main__":
    main()