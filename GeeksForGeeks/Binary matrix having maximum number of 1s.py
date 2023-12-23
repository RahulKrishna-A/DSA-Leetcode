class Solution:
    def findMaxRow(self, mat, N):
        # Code here

        def lowerbound(arr):
            s = 0
            e = len(arr) - 1

            ind = -1
            while s <= e:
                mid = s + (e - s) // 2
                if arr[mid] == 1:
                    e = mid - 1
                    ind = mid

                else:
                    s = mid + 1
            if ind == -1:
                return 0
            else:
                return len(mat) - ind

        max_ones = 0
        max_index = 0
        for i in range(len(mat)):

            cur = lowerbound(mat[i])

            if cur > max_ones:
                max_ones = cur
                max_index = i
            # print(max_ones,max_index)
        return [max_index, max_ones]
