# User function Template for python3

class Solution:
    def countOfSubstrings(self, S, K):
        # code here
        hashmap = {}
        count = 0
        for i in range(K):
            if S[i] in hashmap:
                hashmap[S[i]] += 1
            else:
                hashmap[S[i]] = 1

        if len(hashmap) == K - 1:
            count += 1
        j = 0
        for i in range(K, len(S)):
            if hashmap[S[j]] > 1:
                hashmap[S[j]] -= 1
            else:
                del hashmap[S[j]]
            j += 1
            if S[i] in hashmap:
                hashmap[S[i]] += 1
            else:
                hashmap[S[i]] = 1

            if len(hashmap) == K - 1:
                count += 1
        return count