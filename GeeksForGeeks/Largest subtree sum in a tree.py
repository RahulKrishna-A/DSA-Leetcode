from typing import Optional
from collections import deque

"""

definition of binary tree node.
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""


class Solution:
    def findLargestSubtreeSum(self, root: Optional['Node']) -> int:
        # code here

        maxs = -float("inf")

        def helper(root):
            nonlocal maxs
            if root == None:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            ans = left + right + root.data
            maxs = max(maxs, ans)
            return ans

        helper(root)
        return maxs
