# CS 122 Fall 2025 Lab 6
# Author: Quinn Smiley
# Credit: (None)
# Description: function challenges

#Challenge 1: Collect User Input Lines
def collect_lines(max_lines = 50):
    lines = []
    count = 0

    while True:
        line = input("Line (Enter to stop): ")
        if line == "":
            break

        lines.append(line)
        count += 1

        if count >= max_lines:
            break
    return "\n".join(lines)

# result = collect_lines()
# print("Output (testing):")
# print(result)



#Challenge 2: Count Input Lines
def line_count(transcript):
    count = 0
    current_line = ""

    for char in transcript:
        if char != "\n":
            current_line += char
        else:
            if current_line.strip() != "":
                count += 1
            current_line = ""
    
    if current_line.strip() != "":
        count += 1
    return count

#test = "hello world #sunrise\nsmall steps lead to big changes \n"
# result = line_count(test)
# print("Lines captured (testing): ", result)



#Challenge 3: Find First Word
def first_word(line):
    finder = line.find(" ")
    if finder != -1:
        return line[:finder]
    else:
        return line

#test = "hello world #sunrise"
# result = first_word(test)
# print("first word (testing): ", result)



#Challenge 4: Find First Tag(#)
def extract_tag(line):
    find_tag = line.find("#")
    if find_tag != -1:
        find_space = line.find(" ", find_tag)
        if find_space == -1:
            find_space = len(line)
        return line[find_tag:find_space]
    else:
        return ""
    
# result = extract_tag(test)
# print("tag (testing): ", result)



#Challenge 5: Verify Contains Word
def contains_word(line, word, start=0):
    finder = line.find(word, start)
    if finder != -1:
        return True
    else:
        return False
    
# result = contains_word(test, 'hello')
# print("contains 'hello' (testing)? ", result )



#Challenge 6: Emphasize Word
def emphasize(line, word):
    finder = line.find(word)
    if finder != -1:
        get_word = len(word)
        emphasized = line[:finder] + "[" + word + "]" + line[finder + len(word):]
        return emphasized
    else:
        return line
    
# result = emphasize(test, 'hello')
# print("Emphasis (testing): ", result )

#Challenge 7: Using Uppercase Line and Ensure Terminal Punctuation
def shout(line):
    uppercase = line.upper()
    last = uppercase[-1]
    if last in "!?.":
        return uppercase
    else:
        ex = uppercase + "!"
        return ex
    
# result = shout(test)
# print("Shout (testing): ", result)



#Challenge 8: Remix Input
def remix_line(line):
    first = first_word(line)
    tag = extract_tag(line)
    shouted = shout(line)
    if tag != "":
        remix = tag + " | " + first + " | " + shouted
    else:
        remix = first + " | " + shouted
    return remix

# result = remix_line(test)
# print("Remix (testing): ", result)



#Challenge 9: Implement main()
def main():
    """Orchestrate the String Remix Studio demo.

    Steps (you will fill in during Challenge 9):
    - Call collect_lines() to read input lines (sentinel loop).
    - Print count of lines via line_count().
    - For each complete line (will require rebuilding input by parsing on \n):
        * Print using remix_line()
        * Get first word using first_word()
        * Print => then emphasize()
    """
    # TODO: implement in Challenge 9
    lines = collect_lines()
    num_lines = line_count(lines)
    print("Lines captured: " + str(num_lines))

    lines_list = lines.split("\n")
    for line in lines_list:
        remix = remix_line(line)
        print(remix)

        first = first_word(line)

        emphasized = emphasize(line, first)
        print(f"=> {emphasized}")


# Keep these lines at bottom of the file
# Note: The conditional limits calling main() only when
#       this file is directly executed and not used as 
#       a library
if __name__ == "__main__":
    main()
