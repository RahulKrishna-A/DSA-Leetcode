class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.grid(m,n,{})
    def grid(self,m,n,memo):
        key  = (m,n)
        if key in memo:
            return memo[key]
        if m==1 or n ==1:
            return 1
        c1 = self.grid(m-1,n,memo)
        c2 = self.grid(m,n-1,memo)
        memo[key]=c1+c2
        return memo[key]

