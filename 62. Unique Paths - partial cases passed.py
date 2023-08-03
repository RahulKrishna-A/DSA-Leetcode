class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.maze(m,n)

    def maze(self,r,c):
        if r == 1 or c == 1:
            return 1
        countr = self.maze(r - 1, c)
        countc = self.maze(r, c - 1)

        return countr + countc
