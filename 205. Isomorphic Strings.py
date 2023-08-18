class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        iso = {}
        a = []
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i] in iso:
                if iso[s[i]]==t[i]:
                    continue
                else:
                    return False
            elif t[i] in a:
                return False
            else:
                iso[s[i]]=t[i]
                a.append(t[i])
        return True