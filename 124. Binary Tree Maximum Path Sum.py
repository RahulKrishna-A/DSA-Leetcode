# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    paths = -100000

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def maxsums(node):
            if node == None:
                return 0
            left = maxsums(node.left)
            right = maxsums(node.right)
            left = max(0, left)
            right = max(0, right)
            pre = left + right + node.val
            self.paths = max(pre, self.paths)
            return max(left, right) + node.val

        maxsums(root)
        return self.paths
