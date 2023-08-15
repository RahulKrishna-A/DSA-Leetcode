class Solution(object):
    def fib(self, n, hashs={}):
        """
        :type n: int
        :rtype: int
        """
        if n in hashs:
            return hashs[n]
        if n == 1:
            return 1
        if n == 0:
            return 0

        hashs[n] = self.fib(n - 1, hashs) + self.fib(n - 2, hashs)
        return hashs[n]