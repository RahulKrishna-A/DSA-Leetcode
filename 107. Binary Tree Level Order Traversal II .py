# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        qu = deque()
        result = []
        if root==None:
            return []
        qu.append(root)
        while len(qu)>0:
            levelans = []
            for i in range(len(qu)):
                currentNode = qu.popleft()
                levelans.append(currentNode.val)
                if currentNode.left!=None:
                    qu.append(currentNode.left)
                if currentNode.right!=None:
                    qu.append(currentNode.right)
            result.insert(0,levelans)
        return result