"""Homework 1
Quinn Smiley, 2026-03-31, CS 211"""

import math

class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self): # Used Cursor to understand how to use the __str__ method in the best way
        return f"Point3D({self.x}, {self.y}, {self.z})"

    def euclidean_distance(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        dz = other.z - self.z
        return math.sqrt((dx ** 2) + (dy ** 2) + (dz ** 2))
    
    

if __name__ == "__main__":
    # Test #1
    # p1 = Point3D(1, 2, 3)
    # p2 = Point3D(4, 5, 6)

    # Test #2
    # p1 = Point3D(0, 0, 0)
    # p2 = Point3D(0, 0, 0)

    # Test #3
    p1 = Point3D(-1, -2, -3)
    p2 = Point3D(-4, -5, -6)
    
    if p1.x == p2.x and p1.y == p2.y and p1.z == p2.z:  # Used Cursor to debug my testing
        print(f"Distance between {p1} and itself: {p1.euclidean_distance(p2)}")
    else: 
        print(f"Distance between {p1} and {p2}: {p1.euclidean_distance(p2)}")
    

