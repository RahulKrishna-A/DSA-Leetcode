# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        inor = preorder[:]
        inor.sort()

        def helper(inor, pre):
            if len(inor) == 0 or len(pre) == 0:
                return

            cur = pre[0]
            index = inor.index(cur)
            root = TreeNode(cur)
            root.left = helper(inor[:index], pre[1:index + 1])
            root.right = helper(inor[index + 1:], pre[index + 1:])

            return root

        return helper(inor, preorder)
