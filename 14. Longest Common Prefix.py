class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        lp = ""
        v = sorted(strs)
        s = v[0]
        l= v[-1]
        lns = min(len(s),len(l))
        for i in range(lns):
            if s[i]==l[i]:
                lp+=s[i]
            else:
                return lp
        return lp
