"""
Project 10 solution
Author: Quinn Smiley
Date: 02/25/2026
"""
import math

def count_smaller(lst: list, item: int) -> int:
    # TODO: implement this function
    if lst == []:
        return 0
    if lst[0] < item: 
        return 1 + count_smaller(lst[1:], item)
    else: 
        return count_smaller(lst[1:], item)
# print(count_smaller([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
# print(count_smaller([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))
# print(count_smaller([], 5))


def is_palindrome(s: str) -> bool:
    # TODO: implement this function
    if s == "":
        return True
    if s[0] != s[-1]:
        return False
    else: 
        return is_palindrome(s[1:-1])
    

# print(is_palindrome("racecar"))
# print(is_palindrome("racecars"))


def avg_word_length(lst: list) -> float:
    # TODO: implement this function
    if lst == []:
        return 0.0
    if len(lst) == 1:
        return float(len(lst[0]))
    
    n = len(lst)

    rest_avg = avg_word_length(lst[1:])
    rest_sum = (n - 1) * rest_avg
    total_sum = len(lst[0]) + rest_sum

    return round((total_sum / n), 1)

# print(avg_word_length(['hello', 'world']))
# print(avg_word_length(['hello', 'world', 'meh']))
    
def flatten(a_list: list) -> list:
    if a_list == []:
        return []

    first = a_list[0]
    rest = a_list[1:]

    if type(first) is list:
        return flatten(first) + flatten(rest)
    else:
        return [first] + flatten(rest)
    
# print(flatten([1, 2, 3]))
# print(flatten([1, [2, 3], 4]))
# print(flatten([1, [2, [3, 4, [5], 6], 7], 8]))
