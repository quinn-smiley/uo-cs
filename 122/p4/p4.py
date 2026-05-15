# CS 122 Fall 2025 Project 4
# Author: Quinn SMiley
# Credit: None
# Description: Compounding functions

def get_length(text):
    """Return the length of the given text without using len().

    Requirements:
    - Traverse the string using a for loop and count characters.
    - Return the final count as an int.
    """
    # TODO: loop over text, count characters, return count (no len()).
    count = 0
    for ch in text:
        count += 1
    return count

#print(get_length("Test"))

    


def is_vowel(ch):
    """Return True if ch is a vowel, False otherwise.

    Requirements:
    - Treat 'a', 'e', 'i', 'o', 'u' (both lowercase and uppercase) as vowels.
    - Use a for loop over a constant string of vowels and compare characters.
    - Return True/False accordingly.
    """
    vowels = "aeiouAEIOU"
    # TODO: compare ch against a string of vowels using a for loop.
    for i in vowels: 
        if ch == i:
            return True
    return False
        
#print(is_vowel("a"))
#print(is_vowel("h"))

def is_letter_in_text(letter, text):
    """Return True if letter is found in text, False otherwise.

    Requirements:
    - Traverse text with a for loop; compare each character to letter.
    - Return True immediately when found; otherwise False at the end.
    """
    # TODO: search for letter in text using a for loop and conditionals.
    for ch in text: 
        if ch ==letter:
            return True
    return False
        
#print(is_letter_in_text("a", "apple"))
#print(is_letter_in_text("h", "apple"))


def get_vowels(text):
    """Return a string containing only the vowels from the given text.

    Requirements:
    - Return only UNIQUE vowels, preserving the order of FIRST appearance.
    - Preserve the original case of each vowel you include.
    - Use is_vowel(ch) to test for vowel.
    - Use is_letter_in_text(ch, result) == False to prevent duplicates.
    - Build the result via string concatenation in a for loop.
    """
    # TODO: build a string of unique vowels discovered in order.
    result = ''
    for ch in text: 
        if is_vowel(ch) == True and is_letter_in_text(ch, result) == False:
            result += ch
    return result

#print(get_vowels("Testing"))



def count_letter_in_text(letter, text):
    """Return the count of how many times letter appears in text.

    Requirements:
    - Traverse the text with a for loop.
    - Count matches with 'if ch == letter:'.
    - Return the final count as an int.
    """
    # TODO: count occurrences of letter in text.
    count = 0
    for ch in text:
        if ch == letter:
            count += 1
    return count

#print(count_letter_in_text("t", "tester"))



def main():
    """Main program logic.

    Steps / Requirements:
    - Prompt the user for input text with input("Enter some data: ").
    - Call get_length(text) and print: "Length of data is:", <length>.
    - Call get_vowels(text) and print: "Vowels in data are:", <vowel_string>.
    - Use a for loop over the vowel_string to iterate each vowel.
    - For each vowel, call count_letter_in_text(vowel, original_text)
      and print: "Letter '<vowel>' occurs <count> time(s)."
    - Use only Chapter 5 features (see constraints at top of file).
    """
    # TODO: prompt for input text
    # TODO: compute length via get_length and print result
    # TODO: compute unique vowels via get_vowels and print result
    # TODO: for each vowel in the vowel_string:
    #           compute count via count_letter_in_text
    #           print the formatted line for that vowel
    text = input("Enter some data: ")

    length = get_length(text)
    print("Length of data is:", length)

    vowels = get_vowels(text)
    print("Vowels in data are:", vowels)

    for ch in vowels: 
        count = count_letter_in_text(ch, text)
        print("Letter '" + ch + "' occurs " + str(count) + " time(s).")


# Entry point (uncomment when ready to run your implementation)
main()