# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        Ans = []
        temp = root
        if root == None:
            return []

        def inorder(node, cur_ans):
            cur_ans.append(node.val)
            if node.left == None and node.right == None:
                string = str(cur_ans[0])
                for i in range(1, len(cur_ans)):
                    string = string + "->" + str(cur_ans[i])
                Ans.append(string)

            if node.left != None:
                inorder(node.left, cur_ans)
                cur_ans.pop()
            if node.right != None:
                inorder(node.right, cur_ans)
                cur_ans.pop()

        inorder(temp, [])
        return Ans
