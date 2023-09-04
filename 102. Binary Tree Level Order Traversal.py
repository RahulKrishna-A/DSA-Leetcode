# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        ans = []
        qu = deque()
        qu.append(root)

        while len(qu) > 0:
            currentans = []
            for i in range(len(qu)):
                currentNode = qu.popleft()
                currentans.append(currentNode.val)
                if currentNode.left != None:
                    qu.append(currentNode.left)
                if currentNode.right != None:
                    qu.append(currentNode.right)
            ans.append(currentans)
        print(ans)
        return ans