# User function Template for python3

class Solution:

    # Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        # code here
        i = 0
        j = n - 1

        while i < j:
            if M[i][j] == 1:
                i += 1
            else:
                j -= 1

        cand = i
        for k in range(n):
            if k != i:
                if M[cand][k] == 1 or M[k][cand] == 0:
                    return -1
        return i


