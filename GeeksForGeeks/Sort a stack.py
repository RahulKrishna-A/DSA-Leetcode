class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack

    def Sorts(self, s, X):
        if len(s) == 0 or s[-1] <= X:
            s.append(X)
            return s
        else:
            temp = s.pop()
            self.Sorts(s, X)
            s.append(temp)
        return s

    def Sorted(self, s):
        # Code9s !=0here
        if len(s) != 0:
            temp = s.pop()
            self.Sorted(s)
            self.Sorts(s, temp)
        return s


