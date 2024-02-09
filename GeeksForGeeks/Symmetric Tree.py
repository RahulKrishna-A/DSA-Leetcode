# User function Template for python3

class Solution:
    # return true/false denoting whether the tree is Symmetric or not
    def isSymmetric(self, root):
        # Your Code Here
        if root == None:
            return True

        def isIdentical(node1, node2):
            if node1 == None and node2 == None:
                return True
            if node1 == None or node2 == None:
                return False
            if node1.data != node2.data:
                return False
            return isIdentical(node1.left, node2.right) and isIdentical(node1.right, node2.left)

        return isIdentical(root.left, root.right)
