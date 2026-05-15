class Stack:
    """
    A simple implementation of a stack data structure.
    Methods:
        __init__():
            Initializes an empty stack.
        push(item):
            Adds an item to the top of the stack.
        pop():
            Removes and returns the item from the top of the stack.
            Raises:
                IndexError: If the stack is empty.
        is_empty():
            Checks if the stack is empty.
            Returns:
                bool: True if the stack is empty, False otherwise.
    """

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty(): 
            raise IndexError("Popped on empty stack")
        else: 
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


class State:
    """
    Represents the state of a turtle in a 2D coordinate system.
    Attributes:
        x (float): The x-coordinate of the state.
        y (float): The y-coordinate of the state.
        angle (float): The angle (in degrees) representing the direction of the state.
    Methods:
        __str__():
            Returns a string representation of the state in the format "(x, y, angle)".
        __repr__():
            Returns a string representation of the state in the format "(x, y, angle)".
        set_state(t):
            Updates the state based on the position and heading of a given turtle object.
            Args:
                t (turtle.Turtle): A turtle object whose position and heading will be used to update the state.
    """

    def __init__(self, x=0, y=0, angle=0):
        self.x = x
        self.y = y
        self.angle = angle

    def __str__(self):
        return f"({self.x}, {self.y}, {self.angle})"

    def __repr__(self):
        return f"State({self.x}, {self.y}, {self.angle})"

    def set_state(self, t):
        [self.x, self.y] = t.pos()
        self.angle = t.heading


if __name__ in "__main__":
    stack = Stack()
    state = State(6, 7, 90)


    print(stack.push(state))
    print(str(state))
    print(repr(state))
