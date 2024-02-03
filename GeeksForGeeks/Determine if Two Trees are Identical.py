class Solution:
    # Function to check if two trees are identical.
    def isIdentical(self, root1, root2):
        # Code here
        if root1 == None and root2 == None:
            return True
        if root1 == None or root2 == None:
            return False
        if root1.data != root2.data:
            return False

        return self.isIdentical(root1.left, root2.left) and self.isIdentical(root1.right, root2.right)
