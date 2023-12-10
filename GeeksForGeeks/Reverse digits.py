class Solution:
    def reverse_digit(self, n):
        # Code here
        ans = 0
        while n > 0:
            last = n % 10
            n //= 10
            ans = ans * 10 + last
        return ans
