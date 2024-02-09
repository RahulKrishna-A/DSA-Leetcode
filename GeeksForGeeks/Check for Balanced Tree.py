# User function Template for python3


'''class Node: 
    # Constructor to create a new Node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None'''


# Function to check whether a binary tree is balanced or not.
class Solution:
    def isBalanced(self, root):

        # add code here
        def height(node):
            if node == None:
                return 0
            left = height(node.left)
            right = height(node.right)
            if left == -1 or right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            return max(left, right) + 1

        return False if height(root) == -1 else True