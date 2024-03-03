# Node class

class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None


class Solution:
    def buildtree(self, inorder, preorder, n):
        # code here
        # build tree and return root node
        if len(inorder)==0 or len(preorder)==0:
            return

        ele = preorder[0]
        mid = inorder.index(ele)
        node  = Node(ele)
        node.left = self.buildtree(inorder[:mid],preorder[1:mid+1],n)
        node.right = self.buildtree(inorder[mid+1:],preorder[mid+1:],n)
        return node
