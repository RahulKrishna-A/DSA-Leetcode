# User function Template for python3
class Solution:

    def search(self, pat, txt):
        # code here
        need = {}
        have = {}
        left = 0
        for i in pat:
            need[i] = need.get(i, 0) + 1
        count = 0
        min_count = len(pat)

        for i in range(len(txt)):
            have[txt[i]] = have.get(txt[i], 0) + 1
            if i >= min_count - 1:

                if have == need:
                    count += 1
                if have[txt[left]] == 1:
                    del have[txt[left]]
                else:
                    have[txt[left]] -= 1
                left += 1
        return count