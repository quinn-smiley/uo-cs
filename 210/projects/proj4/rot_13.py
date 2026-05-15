# def encrypt(msg):
def encrypt(msg):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    for char in msg.lower(): 
        i = 0
        found = False
        while i < 26:
            if char == alphabet[i]:
                new = (i + 13) % 26
                result += alphabet[new]
                found = True
                break
            i += 1
        if not found:
            result += char


    return result

#encrypted = encrypt("Two driven jocks help fax my big quiz")

def decrypt(msg):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    for char in msg: 
        i = 0
        found = False
        while i < 26:
            if char == alphabet[i]:
                original = (i - 13) % 26
                result += alphabet[original]
                found = True
                break
            i += 1
        if not found: 
            result += char

    return result

#print(decrypt(encrypted))

#Tests: 
