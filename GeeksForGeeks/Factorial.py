#User function Template for python3


class Solution:
    def factorial (self, N):
        # code here
        if N==0 or N==1:
            return 1
        return N*self.factorial(N-1)