"""Shape3D class
Quinn Smiley, 2026-04-14, CS 211"""

import math

class Shape3D:
    def __init__(self):
        raise NotImplementedError("Abstract class cannot be instantiated")
    
    def volume(self) -> float:
        raise NotImplementedError("Not implemented for abstract class")
    
    def area(self) -> float:
        raise NotImplementedError("Not implemented for abstract class")
    
    def print_info(self): # Asked Cursor how to format the output correctly
        area = round(self.area(), 4)
        volume = round(self.volume(), 4)
        print(f"Area: {area}, Volume {volume}")
    

class Cylinder(Shape3D):
    def __init__(self, radius: float, height: float):
        assert isinstance(radius, float) and isinstance(height, float)
        self.radius = radius
        self.height = height

    def volume(self):
        return math.pi * (self.radius ** 2) * self.height
    
    def area(self):
        return (2 * math.pi * (self.radius ** 2)) + (2 * math.pi * self.radius * self.height)


class Cuboid(Shape3D): 
    def __init__(self, w, l, h):
        assert isinstance(w, float) and isinstance(l, float) and isinstance(h, float)
        self.w = w
        self.l = l
        self.h = h

    def volume(self):
        return self.w * self.l * self.h
    
    def area(self):
        return (2 * self.w * self.l) + (2 * self.w * self.h) + (2 * self.l * self.h)
        

class Cube(Cuboid):
    def __init__(self, w):
        assert isinstance(w, float)
        super().__init__(w, w, w)



if __name__ == "__main__":
    cyl = Cylinder(3.0,5.0)
    cuboid = Cuboid(6.0,4.0,9.0)
    lst = [Cube(3.0), cyl, cuboid]
    for shape in lst:
        shape.print_info()


    