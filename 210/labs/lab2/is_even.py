# File: is_even.py
def is_even(n):
    """ Determines if n is an even number.
    Args:
    n: an integer number
    Returns:
    True if n is an even number, False otherwise
    >>> is_even(100)
    True
    >>> is_even(101)
    False
    >>> is_even(0)
    True
    """
    return (n % 2) == 0

#print(is_even(2))
result = is_even(3)
#print(result)

def welcome():
    """Print a welcome message.
    >>> welcome()
    Good morning, CS 210!
    """
    print('Good morning, CS 210!')
    return None
welcome()

check = welcome()
check
print(check)
print(welcome())