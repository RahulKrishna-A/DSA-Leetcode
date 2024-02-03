# User function Template for python3


class Solution:
    max_dia = 0

    # Function to return the diameter of a Binary Tree.
    def diameter(self, root):
        # Code here
        def diam(root):
            if root == None:
                return 0

            left = diam(root.left)
            right = diam(root.right)
            dia = left + right + 1
            self.max_dia = max(self.max_dia, dia)
            return max(left, right) + 1

        diam(root)
        return self.max_dia
