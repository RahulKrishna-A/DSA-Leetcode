# User function Template for python3


class Solution:

    # Function to rotate matrix anticlockwise by 90 degrees.
    def rotateby90(self, a, n):
        # code here

        for i in a:
            s = 0
            e = len(i) - 1
            while s < e:
                i[s], i[e] = i[e], i[s]
                s += 1
                e -= 1

        for i in range(n):
            for j in range(i + 1, n):
                a[i][j], a[j][i] = a[j][i], a[i][j]

        return a