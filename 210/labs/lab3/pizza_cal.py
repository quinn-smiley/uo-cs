import math
import doctest

def circle_area(r):
    '''
    (int) -> float
    Calculates and returns the area of a circle given the radius.
    Examples:
    >>> circle_area(5)
    78.53981633974483
    >>> circle_area(10)
    314.1592653589793
    '''
    area = math.pi * r**2
    return area

#print(circle_area(10))

def pizza_CPSI(diameter, cost):
    '''
    (int, num) -> float
    Calculates and returns the cost per square inch,
    given the diameter and cost of a pizza.
    Examples:
    >>> pizza_CPSI(14, 18)
    0.117
    >>> pizza_CPSI(14, 20.25)
    0.132
    '''
    r = diameter / 2
    area = circle_area(r)
    cost_per_inch = cost / area
    cost_per_inch = round(cost_per_inch, 3)
    return cost_per_inch

# diameter = 20
# cost = 31.42
# print(pizza_CPSI(diameter, cost))

print(doctest.testmod())