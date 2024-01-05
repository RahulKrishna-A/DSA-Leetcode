# User function Template for python3

class Solution:

    # Function to check if brackets are balanced or not.
    def ispar(self, x):
        # code here
        stacks = []
        for i in x:
            if i == "[" or i == "{" or i == "(":
                stacks.append(i)
            else:
                if len(stacks) > 0 and ((stacks[-1] == "[" and i == "]") or (stacks[-1] == "{" and i == "}") or (
                        stacks[-1] == "(" and i == ")")):
                    stacks.pop()
                else:
                    return 0
        return 1 if len(stacks) == 0 else 0

