"""Fraction class
Quinn Smiley, 2026-03-31, CS 211"""


def gcd(a, b):
    if a == b: 
         return a
    if a < b: 
         (a, b) = (b, a)
    return gcd(a - b, b)

class Fraction:
    def __init__(self, num, den):
        assert num >= 0
        assert den > 0
        assert isinstance(num, int) and isinstance(den, int)

        self.num = num
        self.den = den

    def __str__(self):
        return f"{self.num}/{self.den}"
    
    def __repr__(self):
        return f"Fraction({self.num}, {self.den})"
    
    def __add__(self, other):
        new_n = (self.num * other.den) + (other.num * self.den)
        new_d = self.den * other.den
        newFract = Fraction(new_n, new_d)
        return newFract
    
    def __mul__(self, other):
        new_n = self.num * other.num
        new_d = self.den * other.den
        newFract = Fraction(new_n, new_d)
        return newFract
    
    def simplify(self):
        self_gcd = gcd(self.num, self.den)
        simple_num = int(self.num / self_gcd)
        simple_den = int(self.den / self_gcd)
        return Fraction(simple_num, simple_den)
    


if __name__ == "__main__":
    print("Fraction tests")

    f1 = Fraction(6,10)
    f2 = Fraction(1, 2)

    # str test
    print(str(f1))

    # repr test
    print(repr(f1))

    # add test
    print(f"{f1} + {f2} = {f1 + f2}")

    # mul test
    print(f"{f1} * {f2} = {f1 * f2}")

    # simplify test
    print(f1.simplify())
    print(f2.simplify())
