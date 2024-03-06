class Solution:

    # Function to return a list of indexes denoting the required
    # combinations whose sum is equal to given number.
    def combinationalSum(self, A, B):

        res = []

        def helper(temp, i, bal):
            if i == len(A):
                if bal == 0:
                    res.append(temp[:])
                return

            if A[i] <= bal:
                temp.append(A[i])
                helper(temp, i, bal - A[i])
                temp.pop()

            helper(temp, i + 1, bal)

        helper([], 0, B)
        return res