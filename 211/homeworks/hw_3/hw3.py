"""Homework 3
Quinn Smiley, 2026-04-20, CS 211"""

class Kaprekar:
    kaprekar_constant = 6174 # a class variable or member

    def __init__(self, number): # Asked Cursor the best way to structure the constructor. 
        self.number = 0
        self.digits = []
        self.set_number(number)

    def __str__(self):
        s = str(self.number)
        while len(s) < 4:
            s = "0" + s
        return s

    def __repr__(self):
        return f"Kaprekar({self.__str__()})"

    def set_number(self, number):
        s = str(number)
        while len(s) < 4:
            s = "0" + s
        self.number = int(s)
        self.digits = []
        for ch in s:
            self.digits.append(int(ch))
        

    def is_kaprekar(self):
        return self.number == Kaprekar.kaprekar_constant

    def largest(self):
        d = self.digits[:] 
        d.sort()
        d.reverse()

        value = 0
        for digit in d:
            value = value * 10 + digit
        return value

    def smallest(self):
        d = self.digits[:]
        d.sort()

        value = 0
        for digit in d:
            value = value * 10 + digit
        return value

    def step(self):
        big = self.largest()
        small = self.smallest()
        result = big - small
        self.set_number(result)
        return result

    def kaprekar_steps(self):
        steps = 0
        while steps < 100:
            if self.is_kaprekar():
                return steps

            if len(set(self.digits)) < 2:
                return 100

            self.step()
            steps += 1

        return 100

if __name__ == "__main__":
    print(f"Kaprekar constant: {Kaprekar.kaprekar_constant}")
    n = input("Enter a 4-digit number: ")

    if len(n) != 4 or not n.isdigit():
        print("Please enter a valid 4-digit number.")
        exit(1)

    k = Kaprekar(int(n))
    print(k)

    print(f"Number of steps to reach Kaprekar constant: {k.kaprekar_steps()}")
    print(f"Is Kaprekar constant: {k.is_kaprekar()}")

   # 5200 -> 7
   # 1234 -> 3
   # 8894 -> 6
   # 5757 -> 6
   # 1111 -> 100
   # 6174 -> 0