"""
class designed to represent an image as a Quad Tree.

Juan Flores
5/20/23
"""
from binary_matrix import *
from math import inf as infinity


class QuadTree:

    def __init__(self, depth=0, mean=0, size=0) -> None:
        """
        Initializes a new QuadTree node with default values.
        """
        self.depth = depth
        self.mean = mean
        self.size = size
        self.nw = None
        self.ne = None
        self.se = None
        self.sw = None


    def insert(self, bin_mat, depth=0):
        """
        Recursively inserts a binary matrix into the QuadTree, splitting it into quadrants
        if the matrix contains mixed bits.
        """
        self.depth = depth
        self.mean = matrix_mean(bin_mat)
        self.size = len(bin_mat)

        if same_bits(bin_mat):
            return
        
        [nw, ne, se, sw] = split_4(bin_mat)

        self.nw = QuadTree(depth + 1, 0, 0)
        self.ne = QuadTree(depth + 1, 0, 0)
        self.se = QuadTree(depth + 1, 0, 0)   
        self.sw = QuadTree(depth + 1, 0, 0)

        self.nw.insert(nw, depth + 1)
        self.ne.insert(ne, depth + 1)
        self.se.insert(se, depth + 1)
        self.sw.insert(sw, depth + 1)



    def reconstruct_image(self, depth):
        """
        Reconstructs the binary matrix from the QuadTree up to a specified depth.
        """
        if self.nw == None or self.depth == depth: 
            return [[self.mean] * self.size for _ in range(self.size)]

        nw = self.nw.reconstruct_image(depth)
        ne = self.ne.reconstruct_image(depth)
        se = self.se.reconstruct_image(depth)
        sw = self.sw.reconstruct_image(depth)

        return stitch_matrices(nw, ne, se, sw)


    def __str__(self): # Asked Cursor the best way to achievce the format
        """
        Returns a string representation of the QuadTree, including its depth, mean, size, and child nodes.
        """
        num_plus = "+" * self.depth
        if self.depth > 0: 
            num_plus += " "
        result = f"{num_plus}(({self.depth}, {self.mean}, ({self.size}, {self.size})))\n"

        for child in (self.nw, self.ne, self.se, self.sw):
            if child is not None: 
                result += str(child)

        return result



if __name__ == "__main__":
    binary_file = 'images/fisherman.txt'
    matrix = read_bin_matrix(binary_file)
    q_t = QuadTree()
    q_t.insert(matrix)
    # print(q_t)

    depth = infinity  # why infinity?
    rec_mat = q_t.reconstruct_image(depth)
    plot_bin_matrix(rec_mat)
