def encrypt(msg): 
    even = ""
    odd = ""
    count = 0
    for ch in msg:
        if count % 2 == 0:
            even = even + ch
        else:
            odd = odd + ch
        count = count + 1
    cipher = odd + even
    return cipher

# print(encrypt("It was a dark and stormy night"))

def decrypt(msg):
    half = len(msg) // 2
    odd = msg[:half]
    even = msg[half:]
    plain_txt = ""

    for i in range(half):
        plain_txt = plain_txt + even[i]
        plain_txt = plain_txt + odd[i]

    if len(even) > len(odd):
        plain_txt = plain_txt + even[-1]

    return plain_txt

# print(decrypt("twsadr n tryngtI a  akadsom ih"))


