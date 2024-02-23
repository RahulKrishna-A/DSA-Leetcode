class Solution:

    # Function to find the least absolute difference between any node
    # value of the BST and the given integer.
    def minDiff(self, root, K):
        # code here
        mins = float("inf")

        def helper(root, K):
            nonlocal mins
            if root == None:
                return root
            if root.data == K:
                mins = 0
                return
            mins = min(mins, abs(root.data - K))
            if root.data > K:
                helper(root.left, K)
            else:
                helper(root.right, K)

        helper(root, K)
        return mins
