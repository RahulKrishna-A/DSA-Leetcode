class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        s= 0
        e=len(matrix)*len(matrix[0])-1
        columnno= len(matrix[0])
        while s<=e:
            mid = s + (e-s)//2
            r = mid//columnno
            c=mid % columnno
            if matrix[r][c]==target:
                return True
            if matrix[r][c]>target:
                e =mid-1
            else:
                s=mid+1
        return False
