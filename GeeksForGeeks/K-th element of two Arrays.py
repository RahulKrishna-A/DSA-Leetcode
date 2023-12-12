# User function Template for python3

class Solution:
    def kthElement(self, arr1, arr2, n, m, k):
        count = 0
        i, j = 0, 0
        while i < n and j < m:
            count += 1
            if arr1[i] < arr2[j]:
                if count == k:
                    return arr1[i]
                i += 1
            else:
                if count == k:
                    return arr2[j]
                j += 1
        while i < n:
            count += 1
            if count == k:
                return arr1[i]
            i += 1

        while j < m:
            count += 1
            if count == k:
                return arr2[j]
            j += 1
