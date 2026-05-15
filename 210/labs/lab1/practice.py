# CIS 210 Lab 1 – Lab 1 Exercises
# Author: Quinn Smiley
# Credits: [acknowledgements - lab group, perhaps others]
# Lab exercises demonstrating how VSCode Editor and Shell interact.

phrase = "Coding is fun!"
vowels = "aeiou"
result = ""
for char in phrase.lower():
    if char not in vowels and char.isalpha():
        result += char
    else:
        result += "_"

print(result)
