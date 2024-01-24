class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        maxs = 0
        left = 0
        for i in range(len(s)):
            hashmap[s[i]] = hashmap.get(s[i], 0) + 1
            while i - left + 1 - max(hashmap.values()) > k:
                hashmap[s[left]] -= 1
                left += 1

            maxs = max(maxs, i - left + 1)
        return maxs
