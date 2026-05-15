"""Node class
Quinn Smiley, 2026-04-14, CS 211"""

class Node: 
    def __init__(self, node_data):
        self.node_data = node_data

    def sum_node_data(self):
        raise NotImplementedError
        
    def __str__(self):
        raise NotImplementedError

class Leaf(Node):
    def __init__(self, node_data):
        super().__init__(node_data)

    def sum_node_data(self):
        return self.node_data
    
class Internal(Node):
    def __init__(self, node_data, left, right):
        super().__init__(node_data)
        self.left = left
        self.right = right

    def sum_node_data(self):
        return (self.node_data) + (self.left.sum_node_data()) + (self.right.sum_node_data())

def main():
    l1 = Leaf(3)
    l2 = Leaf(6)
    l3 = Leaf(9)
    i = Internal(7, l2, l3)
    root = Internal(5, l1, i)
    print(root.sum_node_data())

if __name__ == '__main__':
    main()