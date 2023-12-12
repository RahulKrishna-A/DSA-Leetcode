# User function Template for python3

# Function to return the count of the number of elements in
# the intersection of two arrays.
class Solution:
    def NumberofElementsInIntersection(self, a, b, n, m):
        # return: expected length of the intersection array.

        # code here
        hash1 = {}
        count = 0
        b = set(b)
        for i in a:
            if i in hash1:
                hash1[i] += 1
            else:
                hash1[i] = 1
        for i in b:
            if i in hash1:
                count += 1
        return count

