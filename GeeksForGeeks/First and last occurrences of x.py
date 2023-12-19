# User function Template for python3


class Solution:
    def find(self, arr, n, x):

        def occ(choice):
            s = 0
            e = n - 1
            ans = -1
            while s <= e:
                mid = s + (e - s) // 2
                if arr[mid] == x:
                    ans = mid
                    if choice == "first":
                        e = mid - 1
                    else:
                        s = mid + 1
                elif arr[mid] > x:
                    e = mid - 1
                else:
                    s = mid + 1
            return ans

        first = occ("first")
        last = occ("last")
        return [first, last]

