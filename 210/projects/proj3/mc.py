import math
import random

def pi_mc(num_darts: int) -> float:
    in_circle = 0 

    for i in range(num_darts):
        x = random.random()
        y = random.random()

        d = math.sqrt(x**2 + y**2)
        if d <= 1: 
            in_circle = in_circle + 1
        
    pi = in_circle / num_darts * 4
    return pi

# print(pi_mc(5))