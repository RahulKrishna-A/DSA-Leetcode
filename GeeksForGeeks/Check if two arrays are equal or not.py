# User function Template for python3

class Solution:
    # Function to check if two arrays are equal or not.
    def check(self, A, B, N):

        # return: True or False

        # code here
        A1 = {}
        B1 = {}
        for i in A:
            if i in A1:
                A1[i] += 1
            else:
                A1[i] = 1
        for i in B:
            if i in B1:
                B1[i] += 1
            else:
                B1[i] = 1
        if B1 == A1:
            return 1
        else:
            return 0
