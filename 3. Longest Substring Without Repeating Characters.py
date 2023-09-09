class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        ss = set()
        ans = 0
        for i in range(len(s)):
            while s[i] in ss:
                ss.remove(s[start])
                start += 1
            ss.add(s[i])
            print(ss)
            ans = max(ans, len(ss))
        return ans

