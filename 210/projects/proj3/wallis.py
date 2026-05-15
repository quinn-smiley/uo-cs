import math

def pi_wallis(num_pairs: int) -> float: 
    acc = 1
    num = 2

    for a_pair in range(num_pairs):
        left_term = num / (num - 1)
        right_term = num / (num + 1)
        acc = acc * left_term * right_term
        num = num + 2

    pi = acc * 2
    return pi

# print(pi_wallis(5))