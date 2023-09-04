# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root==None:
            return []
        ans = []
        qu = deque()
        qu.append(root)
        while len(qu)>0:
            levelans = []
            for i in range(len(qu)):
                levelNode = qu.popleft()
                levelans.append(levelNode.val)
                if levelNode.left!=None:
                    qu.append(levelNode.left)
                if levelNode.right!=None:
                    qu.append(levelNode.right)
            ans.append(levelans)
        final = []
        for i in ans:
            final.append(sum(i)/len(i))
        return final