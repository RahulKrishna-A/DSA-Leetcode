class Solution(object):
    def isValidSudoku(self, arr):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for r in range(9):
            for c in range(9):
                if arr[r][c] == ".":
                    continue
                if self.isSafe(arr, arr[r][c], r, c):
                    continue
                else:
                    return False
        return True

    def isSafe(self, arr, value, r, c):
        for i in range(9):
            if arr[r][i] != "." and i != c and arr[r][i] == value:
                return False
        for j in arr:
            if j[r] == "." and j != r and j[r] == value:
                return True
        row_start = r - r % 3
        col_start = c - c % 3
        for ro in range(row_start, row_start + 3):
            for co in range(col_start, col_start + 3):
                if ro == r and co == c:
                    continue
                if arr[ro][co] == value:
                    return False
        return True

