
class Solution:

    # Function to find the minimum element in sorted and rotated array.
    def minNumber(self, arr ,low ,high):
        # Your code here
        # print(low,high)
        def pivot():
            s=0
            e=len(arr)-1
            while s<=e:
                mid = s+(e-s)//2
                if mid>s and arr[mid-1]>arr[mid] :
                    return mid
                elif mid<e and arr[mid]>arr[mid+1]:
                    return mid+1

                elif arr[mid]>arr[s]:
                    s=mid+1
                else:
                    e=mid-1
            return -1
        pivot =

        pivot()
        if pivot==-1 :
            return arr[0]
        else:
            return arr[pivot]
