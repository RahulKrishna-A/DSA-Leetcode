# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        reverse = False
        qu = deque()
        final = []
        qu.append(root)
        while len(qu) > 0:
            level = []
            for i in range(len(qu)):
                if reverse == False:
                    currentNode = qu.popleft()
                    level.append(currentNode.val)
                    if currentNode.left != None:
                        qu.append(currentNode.left)
                    if currentNode.right != None:
                        qu.append(currentNode.right)
                else:
                    currentNode = qu.pop()
                    level.append(currentNode.val)
                    if currentNode.right != None:
                        qu.appendleft(currentNode.right)
                    if currentNode.left != None:
                        qu.appendleft(currentNode.left)
            reverse = not reverse
            final.append(level)
        return final




