# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        lists = []

        def helper(node):
            if node == None:
                return

            helper(node.left)
            lists.append(node.val)
            helper(node.right)

        helper(root)
        return lists[k - 1]

