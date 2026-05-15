"""
This module implements a binary search tree (BST) Classes:
    Tree:
        Represents the binary search tree. It manages the root node and provides methods for inserting data and searching for values in the tree.
    Node:
        Represents a single node in the binary search tree. It contains the data and references to its left and right children. It also provides recursive methods for inserting new nodes and searching for values.
"""


class Tree:
    """
    An object of this class represents a binary search tree.
    Attributes:
        root (Node or None): The root node of the binary search tree. Initially set to None.
    """

    def __init__(self):
        """
        Initializes a new instance of the binary search tree to a tree with an empty root node.
        """
        self.root = None

    def insert(self, data):
        """
        Inserts a new node with the given data into the binary search tree.
        If the tree is empty, the new node becomes the root. Otherwise, it delegates the work to the root node.
        """
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
        else:
            self.root.insert(new_node)

    def __str__(self):
        """
        Returns a string representation of the binary search tree. Delegation ...
        """
        return f"T({self.root})"

    def search(self, val):
        """
        Searches for a value in the binary search tree. Delegation ...
        """
        if self.root == None:
            return False
        else:
            return self.root.search(val)

    def height(self):
        """
        Returns the height of the binary search tree.
        The height is defined as the number of edges on the longest path from the root to a leaf node.
        """
        if self.root == None:
            return None
        return self.root.height()
    
    def find_min(self):
        """
        Finds the minimum value in the binary search tree.
        Returns:
            The node with the minimum value.
        """
        if self.root != None: 
            current = self.root
            if current.left: 
                return current.left.find_min()
            else: 
                return self.root


    def find_max(self):
        """
        Finds the maximum value in the binary search tree.
        Returns:
            The node with the maximum value.
        """
        if self.root != None: 
            current = self.root
            if current.right: 
                return current.right.find_min()
            else: 
                return self.root


class Node:
    """
    A class representing a node in a binary search tree.
    Attributes:
        data (any): The value stored in the node.
        right (Node or None): The right child of the node.
        left (Node or None): The left child of the node.
    """

    def __init__(self, data):
        """
        Initializes a new node in a binary search tree. Children are initially set to None.
        """
        self.data = data
        self.right = None
        self.left = None

    def __str__(self):
        """
        Returns a string representation of the binary search tree node. Pre-order traversal.
        """
        return f"({self.data} {self.left} {self.right})"

    def insert(self, node):
        """
        Inserts a new node into the binary search tree.
        Args:
            node (Node): The node (a tree in itself) to be inserted into the tree. 
        """
        if self.data != node.data:
            if node.data < self.data:
                if self.left == None:
                    self.left = node
                else:
                    self.left.insert(node)
            elif self.right == None:
                self.right = node
            else:
                self.right.insert(node)
        return

    def search(self, val):
        """
        Searches for a given value in the binary search tree.
        Args:
            val (any): The value to search for in the tree. 
        Returns:
            bool: True if the value is found in the tree, False otherwise.
        Searches recursively in the left or right subtree based on the value.
        """
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
        if self.right:
            return self.right.search(val)
        return False

    def height(self):
        """
        Returns the height of the binary search tree.
        The height is defined as the number of edges on the longest path from the root to a leaf node.
        """
        left_height = 0
        right_height = 0
        if self.left != None:
            left_height = self.left.height()
        if self.right != None:
            right_height = self.right.height()

        if self.left == None and self.right == None:
            return 0
        else:
            return 1 + max(left_height, right_height)
        

    def find_min(self):
        """
        Finds the minimum value in the binary search tree.
        Returns:
            The node with the minimum value.
        """
        if self.left != None: 
            return self.left.find_min()
        else:
            return self

    def find_max(self):
        """
        Finds the maximum value in the binary search tree.
        Returns:
            The node with the maximum value.
        """
        if self.right != None: 
            return self.right.find_max()
        else: 
            return self


if __name__ == "__main__":
    t1 = Tree()
    [t1.insert(value) for value in [30, 10, 5, 40, 7]]
    print(t1)

    print(t1.search(10))
    print(t1.search(11))
    print(t1.search(40))

    print(t1.height())

    print("=" * 20)
    t2 = Tree()
    [t2.insert(value) for value in [5, 7, 10, 30, 40]]
    print(t2)

    print(t2.search(10))
    print(t2.search(11))
    print(t2.search(40))

    print(t2.height())

    print("=" * 20)
    t3 = Tree()

    [t3.insert(value) for value in [12, 6, 20, 4, 9, 14, 8, 13, 16, 7]]
    print(t3)

    print(t3.search(7))
    print(t3.search(20))
    print(t3.search(14))
    print(t3.search(40))

    print(t3.height())


