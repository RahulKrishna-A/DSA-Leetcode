class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        iso = {}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i] in iso:
                if iso[s[i]]==t[i]:
                    continue
                else:
                    return False
            else:
                iso[s[i]]=t[i]
        return True