class Solution:
    # Return the size of the largest sub-tree which is also a BST
    def largestBst(self, root):
        # code here
        return self.largestBst2(root)[0]

    def largestBst2(self, root):
        if root == None:
            return [0, float("inf"), -float("inf")]  # [Count, Min, Max]

        left = self.largestBst2(root.left)
        right = self.largestBst2(root.right)

        if left[2] < root.data and right[1] > root.data:
            return [left[0] + right[0] + 1, min(left[1], root.data), max(right[2], root.data)]

        else:
            return [max(left[0], right[0]), -float("inf"), float("inf")]