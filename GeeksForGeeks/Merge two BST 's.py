# User function Template for python3
from collections import deque

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''


class Solution:

    # Function to return a list of integers denoting the node
    # values of both the BST in a sorted order.
    def merge(self, root1, root2):
        # code here.

        def inorder(root):
            sorted_BST = []
            qu = deque()
            while True:
                while root:
                    qu.append(root)
                    root = root.left
                if len(qu) == 0:
                    break
                root = qu.pop()
                sorted_BST.append(root.data)
                root = root.right
            return sorted_BST

        # return inorder(root1)
        BST1 = inorder(root1)
        BST2 = inorder(root2)

        i, j = 0, 0
        res = []
        n, m = len(BST1), len(BST2)
        while i < n and j < m:
            if BST1[i] < BST2[j]:
                res.append(BST1[i])
                i += 1
            else:
                res.append(BST2[j])
                j += 1

        while i < n:
            res.append(BST1[i])
            i += 1
        while j < m:
            res.append(BST2[j])
            j += 1
        return res