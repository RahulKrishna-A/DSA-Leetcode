'''
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
'''

from collections import deque


# This function finds predecessor and successor of key in BST.
# It sets pre and suc as predecessor and successor respectively
class Solution:
    def findPreSuc(self, root, pre, suc, key):
        # Your code goes here

        qu = deque()
        while True:
            while root:
                qu.append(root)
                root = root.left

            if len(qu) == 0:
                break
            root = qu.pop()
            # print(root.key)
            if root.key < key:
                pre.key = root.key
                # print(pre)
            if root.key > key:
                suc.key = root.key
                # print(suc)
                break
            root = root.right


