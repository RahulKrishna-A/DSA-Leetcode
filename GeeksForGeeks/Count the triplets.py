# User function Template for python3
class Solution:
    def countTriplet(self, arr, n):
        # code here
        count = 0
        arr.sort()
        for i in range(n - 1, -1, -1):
            j = 0
            k = i - 1
            while j < k:
                if arr[j] + arr[k] == arr[i]:
                    count += 1
                    j += 1
                elif arr[j] + arr[k] < arr[i]:
                    j += 1
                else:
                    k -= 1

    return count

