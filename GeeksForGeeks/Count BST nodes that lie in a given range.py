class Solution:
    def getCount(self, root, low, high):
        ##Your code here
        if root == None:
            return 0

        elif root.data >= low and root.data <= high:
            return 1 + self.getCount(root.left, low, high) + self.getCount(root.right, low, high)

        elif root.data < low:
            return self.getCount(root.right, low, high)
        else:
            return self.getCount(root.left, low, high)