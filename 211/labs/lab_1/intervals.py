"""Closed intervals of integers
Quinn Smiley, 2026-03-31, CS 211"""


class Interval: 
    """An interval [m..n] represents the set of integers from m to n."""
    def __init__(self, low: int, high: int):
        """"""
        # if low > high: 
#             raise ValueError("Low value should be below high value")
        assert low < high, "Low value should be below high value"
        self.low = low
        self.high = high

    def __str__(self):
        return f"({self.low}, {self.high})"

    def __repr__(self):
        return f"Interval({self.low}, {self.high})"
    
    def contains(self, i: int) -> bool: 
        """Integer i is within the closed interval"""
        if i in range(self.low, self.high):
            return True
        else: 
            return False
    
    def overlaps(self, other: "Interval") -> bool: 
        """i.overlaps(j) if i and j have some elements in common"""
        answer = False
        for i in range(other.low, other.high):
            # print(i) 
            if self.contains(i):
                answer = True
        return answer       


    def __eq__(self, other: "Interval") -> bool: 
        """Intervals are equal if they have the same low and high bounds"""
        if self.low != other.low and self.high != self.low: 
            raise ValueError
        else: 
            return True
        
    def join(self, other: "Interval") -> "Interval":
        """
        Create a new Interval that contains the union of elements in self and other. 
        Precondition: seld and other must overlap
        """
        assert (self.overlaps(other)) == True
        lowest = min(self.low, other.low)
        highest = max(self.high, other.high)
        new_In = Interval(lowest, highest)
        return new_In
    


        
        
        
        

if __name__ == "__main__":
    test_1 = Interval(3, 5)
    test_2 = Interval(1, 5)

    #  Test init
    print(f"The high was {test_1.high}, and the low was {test_1.low}.")

    # Test contains
    test_num = 0
    print(f"It is {test_1.contains(test_num)} that {test_num} is between {test_1.high} and {test_1.low}.")
    
    # Test overlaps
    print(f"It is {test_1.overlaps(test_2)} that ({test_1.low}, {test_1.high}) overlaps with ({test_2.low}, {test_2.high}).")

    # Test eq
    # print(test_1.__eq__(test_2))

    # Test join
    print(f"{(test_1.join(test_2)).low, (test_1.join(test_2)).high}, is the joined version of ({test_1.low}, {test_1.high}) and ({test_2.low}, {test_2.high}).")

    # Test Prettier
    print(f"{str(test_1.join(test_2))}, is the joined version of {str(test_1)} and {str(test_2)}.")
    print(f"{repr(test_1.join(test_2))}, is the joined version of {repr(test_1)} and {repr(test_2)}.")