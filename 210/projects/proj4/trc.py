def encrypt(msg):
    rail_1 = ""
    rail_2 = ""
    rail_3 = ""
    count = 0
    
    for ch in msg:
        index = count % 3
        if index == 0:
            rail_1 = rail_1 + ch
        elif index == 1:
            rail_2 = rail_2 + ch
        else:
            rail_3 = rail_3 + ch
        count = count + 1

    cipher = rail_1 + rail_2 + rail_3
    return cipher

#encrypted = encrypt("There is no reason anyone would want a computer in their home.")

def decrypt(msg):
    total = len(msg)
    count = total // 3
    remainder = total % 3

    if remainder == 2:
        rail1_len = count + 1
        rail2_len = count + 1
    elif remainder == 1:
        rail1_len = count + 1
        rail2_len = count
    else:
        rail1_len = count
        rail2_len = count

    rail_1 = msg[0 : rail1_len]
    rail_2 = msg[rail1_len : rail1_len + rail2_len]
    rail_3 = msg[rail1_len + rail2_len : ]

    pos1 = 0
    pos2 = 0
    pos3 = 0
    plaintext = ""

    for index in range(total):
        m = index % 3
        if m == 0:
            plaintext += rail_1[pos1]
            pos1 += 1
        elif m == 1:
            plaintext += rail_2[pos2]
            pos2 += 1
        else:
            plaintext += rail_3[pos3]
            pos3 += 1

    return plaintext

#print(decrypt(encrypted))