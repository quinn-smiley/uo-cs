def hello(first_name):
    '''
    (str) -> "Hello, (str)!"
    Takes in the first_name parameter and returns "Hello, first_name!"
    Example: 
    >>> hello("Quinn")
    Hello, Quinn!
    '''
    print("Hello, " + first_name + "!")
    return None

def ciao(first_name):
    '''
    (str) -> "Ciao, (str)!"
    Takes in the first_name parameter and returns "Ciao, first_name!"
    Example: 
    >>> ciao("Quinn")
    Ciao, Quinn!
    '''
    print("Ciao, " + first_name + "!")
    return None

# print(type(hello))
# print(type(ciao))

def greeting(f, name):
    print('Calling', f.__name__)
    greet = f(name)
    return greet

# greeting(hello, 'Orange')
# greeting(ciao, 'Kiwi')

def add_3(a, b, c):
    return a + b + c

def mult_3(a, b, c):
    return a * b * c

def higher_order(f, a, b, c):
    func = f(a, b, c)
    print("Function:", f.__name__)
    print(f.__name__ + "(" + str(a) + ", " + str(b) + ", " + str(c) + ") = " + str(func))
    print(func)

higher_order(add_3, 1, 2, 3)
higher_order(mult_3, 1, 2, 3)