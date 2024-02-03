# User function Template for python3


'''
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''


# your task is to complete this function
# function should print the left view of the binary tree
# Note: You aren't required to print a new line after every test case


class Solution:
    def isSubTree(self, T, S):
        # Code here
        if S == None:
            return True
        if T == None:
            return False
        if self.isIdentical(T, S):
            return True
        return self.isSubTree(T.left, S) or self.isSubTree(T.right, S)

    def isIdentical(self, root1, root2):
        # Code here
        if root1 == None and root2 == None:
            return True
        if root1 == None or root2 == None:
            return False
        if root1.data != root2.data:
            return False

        return self.isIdentical(root1.left, root2.left) and self.isIdentical(root1.right, root2.right)