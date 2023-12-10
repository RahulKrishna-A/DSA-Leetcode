# User function Template for python3


# Complete this function
class Solution:
    def floorSqrt(self, x):
        # Your code here
        ans = 1
        i = 1
        if x == 0 or x == 1:
            return x

        while ans <= x:
            i += 1
            ans = i * i
        return i - 1

