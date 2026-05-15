import math

def pi_arch(num_sides: int) -> float: 
    inner_angle_B = 360.0 / num_sides
    half_angle_A = inner_angle_B / 2

    half_s = math.sin(math.radians(half_angle_A))
    side_s = half_s * 2

    polygon_circumference = num_sides * side_s
    pi = polygon_circumference / 2
    return pi

# print(pi_arch(5))