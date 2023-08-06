class Solution(object):
    def setZeroes(self, arr):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = [0] * len(arr)
        n = [0] * len(arr[0])
        self.modMatrix(arr, m, n)
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if m[i] == 1 or n[j] == 1:
                    arr[i][j] = 0

    def modMatrix(self, arr, m, n):

        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if arr[i][j] == 0:
                    m[i] = 1
                    n[j] = 1




