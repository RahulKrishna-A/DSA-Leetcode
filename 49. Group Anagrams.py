class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for i in strs:
            lists = [0] * 26
            for j in i:
                lists[ord(j) - ord("a")] += 1
            if tuple(lists) in ans:
                ans[tuple(lists)].append(i)
            else:
                ans[tuple(lists)] = [i]
        return list(ans.values())
