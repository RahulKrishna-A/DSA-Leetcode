class Solution:
    # Function to return the count of number of elements in union of two arrays.
    def doUnion(self, a, n, b, m):
        # code here
        nums = set(a)
        for i in b:
            nums.add(i)
        return len(nums)
