def get_vowel_count(s: str) -> int:
    # TODO: implement this function
    vowels = "aeiouAEIOU"
    if s == "":
        return 0
    elif s[0] in vowels:
        return get_vowel_count(s[1:]) + 1
    else: 
        return get_vowel_count(s[1:])
    
# print(get_vowel_count("hello"))


def multiply(a: float, b: int) -> float:
    # TODO: implement this function
    bf = float(b)
    if bf < 0 or b == 0: 
        return 0
    elif bf >= 0: 
        return multiply(a, bf - 1) + a
    
# print(multiply(2.5, 3))

def deep_reverse(a: list) -> list:
    # TODO: implement this function
    if a == []:
        return []
    last = a[-1]
    if type(last) == list: 
        return [deep_reverse(last)] + deep_reverse(a[:-1])
    else: 
        return [a[-1]] + deep_reverse(a[:-1])
    

print(deep_reverse([1, 2, 3]))
print(deep_reverse([1, [2, 3], 4]))
print(deep_reverse([1, [2, [3, 4], [5, [6, 7], 8]]]))
