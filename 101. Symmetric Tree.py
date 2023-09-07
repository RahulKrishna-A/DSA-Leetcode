# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        qu = deque()
        qu.append(root.left)
        qu.append(root.right)

        while len(qu) > 0:
            left = qu.popleft()
            right = qu.popleft()
            if left == None and right == None:
                continue
            if left == None or right == None:
                return False
            if left.val != right.val:
                return False
            qu.append(left.left)
            qu.append(right.right)
            qu.append(left.right)
            qu.append(right.left)
        return True



