# CIS 210 Project 2
# Author: Quinn Smiley
# Credits: N/A
# Creating fb() and fbloop() functions.

def fb(n):
    '''
    If n is divisible by 3, return “fizz”.
    If it is divisible by 5, return “buzz”.
    If it is divisible by both 3 and 5, return “fizzbuzz”.
    Otherwise, just return the number.

    Parameters:
    n (int): A decimal integer
    Returns:
    n, ‘fizz’, or ‘buzz’
    '''
 # Your implementation goes here.
    if n % 3 == 0 and n % 5 == 0 and n >= 1:
        print('fizzbuzz')
    elif n % 3 == 0:
        print('fizz')
    elif n % 5 == 0:
        print('buzz')
    else:
        print(n)

# fb(1)
# fb(13)
# fb(9)
# fb(10)
# fb(15)


def fbloop(num):
    '''
    Loop from 1 to num executing fb

    Parameters:
    num: the last number to include in the loop
    Returns:
    None
    '''
 # Your implementation goes here.
    for n in range(1, num + 1):
        if n % 3 == 0 and n % 5 == 0:
            print('fizzbuzz')
        elif n % 3 == 0:
            print('fizz')
        elif n % 5 == 0:
            print('buzz')
        else: 
            print(n)
    print('Game Over!')
# execute the function fbloop and make sure you get
# the expected results
if __name__ == '__main__':
    fbloop(15)