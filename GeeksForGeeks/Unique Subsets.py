# User function Template for python3

class Solution:

    # Function to find all possible unique subsets.
    def AllSubsets(self, arr, n):
        # code herefor i
        subs = [[]]
        arr.sort()
        for i in range(n):
            s = 0
            if i != 0 and arr[i] == arr[i - 1]:
                s = e
            e = len(subs)
            new = []
            for j in range(s, e):
                new.append(subs[j] + [arr[i]])

            subs.extend(new)
        return sorted(subs)