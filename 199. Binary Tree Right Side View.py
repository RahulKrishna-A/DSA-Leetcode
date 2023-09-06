# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        qu = deque()
        if root == None:
            return []
        qu.append(root)

        while len(qu) > 0:
            ln = len(qu)
            for i in range(len(qu)):
                currentNode = qu.popleft()
                if i == ln - 1:
                    result.append(currentNode.val)

                if currentNode.left != None:
                    qu.append(currentNode.left)
                if currentNode.right != None:
                    qu.append(currentNode.right)
        return result


