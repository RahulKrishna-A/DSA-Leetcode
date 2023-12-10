
class Solution:
    def evenlyDivides (self, N):
        # code here
        n=N
        count=0
        while n>0:
            DIG = n%10
            n=n//10
            if DIG!=0 and N%DIG==0:
                count+=1
        return count
