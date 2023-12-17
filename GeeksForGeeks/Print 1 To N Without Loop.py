#User function Template for python3

class Solution:
    #Complete this functionif
    def printNos(self,N):
        #Your code here
        if N==0:
            return
        self.printNos(N-1)
        print(N,end=" ")
