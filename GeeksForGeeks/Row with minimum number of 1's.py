class Solution:
    def minRow(self, N, M, A):
        # code here
        ans = -1
        min_ones = float("inf")
        for i in range(N):
            count = 0
            for j in range(M):
                if A[i][j] == 1:
                    count += 1
            if count < min_ones:
                min_ones = count
                ans = i
            # print(count,min_ones)
        return ans + 1



