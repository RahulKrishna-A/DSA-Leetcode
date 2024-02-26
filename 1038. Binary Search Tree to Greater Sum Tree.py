# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        cur = 0

        def helper(root):
            nonlocal cur
            if root == None:
                return

            helper(root.right)
            temp = root.val
            root.val += cur
            cur += temp
            helper(root.left)

        helper(root)
        return root