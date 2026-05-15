# Exam 3 Prep

#Inputs - input()
def greeting():
    name = input("Print name: ")
    print("Hello, " + name + "!")

#greeting()

#Inputs - open()
def count_lines(filename):
    count = 0
    fin = open(filename)
    for line in fin:
        fin.readline()
        count += 1
    fin.close()
    return count

# line = line.strip()
line = "   hello world   \n"
#print("Before strip():", line)

line = line.strip()
#print("After strip():", line)

#Skip empty lines
def count_lines(filename, include_empty_lines = False):
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

#SKip Comments
def count_lines_nc(filename, include_empty_lines = False):
    count = 0
    fin = open(filename)
    for line in fin:
        stripped = line.strip()
        if include_empty_lines:
            count += 1
        else: 
            if stripped != "" and not stripped.startswith("#"):
                count += 1
    fin.close()
    return count


#print(count_lines_nc("sample1.txt"))