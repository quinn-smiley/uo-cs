'''
Testing and debugging
CS 210 Lab 5

Functions need to be tested.
'''
import doctest

def ratsBug(weight, rate):
    '''(number, number) -> tuple

    Return number of weeks it will
    take for a rat to weigh 1.5 times
    as much as its original weight
    (weight > 0) if it gains at rate (rate > 0).

    >>> ratsBug(10, .1)     # normal
    (16.1, 5)
    >>> ratsBug(1, .5)      # edge - just one week
    (1.5, 1)
    '''
    weeks = 0
    target = 1.5 * weight # added this variable to make the while comparison better

    while weight < target :
        weight += weight * rate
        weeks += 1
        
    weight = round(weight, 1)
    return (weight, weeks)

# print(ratsBug(10, .1))
# print(ratsBug(1, .5))

def countSeqBug(astr):
    '''(str) -> int

    Returns the length of the longest recurring
    sequence in astr

    >>> countSeqBug('abccde')  # normal  	
    2
    >>> countSeqBug('')        # edge - empty string
    0
    '''
    if len(astr) != 0:
        prev_item = astr[0]
        dup_ct = 1
        high_ct = 1
    else:
        high_ct = 0
        dup_ct = 0
        
    for i in range(1, len(astr)):
        if astr[i] == prev_item:
            dup_ct += 1
        else:
            prev_item = astr[i]
			
            if dup_ct > high_ct:
                high_ct = dup_ct
            dup_ct = 1

    return high_ct

# print(countSeqBug('abccde'))
# print(countSeqBug(''))

def my_averageBug(dataset):
    '''(str) -> float

    Returns average of values in input string values,
    but zeros do not count at all.  Return 0 if there
    is no real data.
    
    >>> my_averageBug('23')    #normal, no zeros
    2.5
    >>> my_averageBug('203')   #normal, a zero
    2.5
    >>> my_averageBug('0000')  #all zeros
    0
    >>> my_averageBug('1')     #single item string
    1.0
    >>> my_averageBug('05050505')  
    5.0
    '''
    count = 0
    total = 0
    for value in dataset:
        if value != '0':
            total += int(value)
# use int to change string to integer
            count += 1 # put this inside the if statement

    if count == 0: # added this to make sure it did not return 0 as a float
        return 0

    avg = total / count
    return avg

# print(my_averageBug('23'))
# print(my_averageBug('203'))
# print(my_averageBug('0000'))
# print(my_averageBug('1'))
# print(my_averageBug('05050505'))


print(doctest.testmod())
