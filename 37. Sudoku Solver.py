class Solution(object):
    def solveSudoku(self, board):
        self.solve(board)
        return board

    def isSafe(self, arr, r, c, num):
        for i in range(len(arr)):
            if arr[r][i] != "." and int(arr[r][i]) == num:
                return False
        for j in arr:
            if j[c] != "." and int(j[c]) == num:
                return False

        sqrt = int(len(arr) ** 0.5)
        row_start = r - r % sqrt
        col_start = c - c % sqrt
        for ro in range(row_start, row_start + sqrt):
            for co in range(col_start, col_start + sqrt):
                if arr[ro][co] != "." and int(arr[ro][co]) == num:
                    return False
        return True

    def solve(self, arr):
        empty = True
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i][j] == ".":
                    r = i
                    c = j
                    empty = False
                    break
            if (empty == False):
                break
        if empty == True:
            return True
        for num in range(1, 10):
            if self.isSafe(arr, r, c, num):
                arr[r][c] = str(num)
                if self.solve(arr):
                    return True
                else:
                    arr[r][c] = "."
        return False

