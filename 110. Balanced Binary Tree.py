# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def Balanced(root):
            if root == None:
                return 0

            leftheight = Balanced(root.left)
            if leftheight == -1:
                return -1

            rightheight = Balanced(root.right)
            if rightheight == -1:
                return -1

            if abs(leftheight - rightheight) > 1:
                return -1

            return max(leftheight, rightheight) + 1

        return Balanced(root) != -1


