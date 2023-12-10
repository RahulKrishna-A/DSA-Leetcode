class Solution:
    #Function to find triplets with zero sum.
    def findTriplets(self, arr, n):
        #code here
        arr.sort()
        for i in range(len(arr)):
            j=i+1
            k=n-1
            while j<k:
                sums = arr[i]+arr[j]+arr[k]
                if sums==0:
                    return 1
                elif sums>=0:
                    k-=1
                elif sums<0:
                    j+=1
        return 0
