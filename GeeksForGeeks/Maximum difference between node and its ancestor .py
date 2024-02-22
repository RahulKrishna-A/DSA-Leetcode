# Function to return the maximum difference between any node and its ancestor.
def maxDiff(root):
    def maxDiffUtil(t, res):

        if (t == None):
            return float("inf"), res

        if (t.left == None and t.right == None):
            return t.data, res

        a, res = maxDiffUtil(t.left, res)
        b, res = maxDiffUtil(t.right, res)
        val = min(a, b)

        res = max(res, t.data - val)

        return min(val, t.data), res

    res = -float("inf")
    x, res = maxDiffUtil(root, res)
    return res