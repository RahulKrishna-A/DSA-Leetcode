
'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    def countPair(self,h1,h2,n1,n2,x):
        '''
        h1:  head of linkedList 1
        h2:  head of linkedList 2
        n1:  len of  linkedList 1
        n2:   len of linkedList 1
        X:   given sum
        '''
        temp =h1
        hashs={}
        counts=0
        while temp:
            if temp.data in hashs:
                hashs[temp.data]+=1
            else:
                hashs[temp.data]=1
            temp = temp.next
        while h2:
            if x-h2.data in hashs:
                counts+=1
            h2=h2.next
        return counts