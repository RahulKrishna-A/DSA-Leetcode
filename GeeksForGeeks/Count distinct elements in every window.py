class Solution:
    def countDistinct(self, A, N, K):
        # Code here
        hashmap = {}
        Dist_arr = []
        for i in range(K):
            if A[i] in hashmap:
                hashmap[A[i]] += 1
            else:
                hashmap[A[i]] = 1
        Dist_arr.append(len(hashmap))
        i = 0
        j = K
        while j <= N - 1:
            if A[j] in hashmap:
                hashmap[A[j]] += 1
            else:
                hashmap[A[j]] = 1
            if hashmap[A[i]] > 1:
                hashmap[A[i]] -= 1
            else:
                del hashmap[A[i]]
            i += 1
            j += 1
            Dist_arr.append(len(hashmap))
        return Dist_arr

