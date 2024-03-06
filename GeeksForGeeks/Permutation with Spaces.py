class Solution:
    def permutation(self, S):
        # code here
        ans = []

        def perma(p, up):
            if up == "":
                ans.append(p)
                return

            perma(p + " " + up[0], up[1:])
            perma(p + up[0], up[1:])

        perma(S[0], S[1:])
        return ans


