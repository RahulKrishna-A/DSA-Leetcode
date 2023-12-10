class Solution:
    def is_palindrome(self, n):
        # Code here
        N = n
        rev = 0
        while N:
            last = N % 10
            N //= 10
            rev = rev * 10 + last
        if rev == n:
            return "Yes"
        return "No"
