class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        for k in matrix:
            i=0
            j=len(k)-1
            while i<j:
                k[i],k[j]=k[j],k[i]
                i+=1
                j-=1

