class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        lists=[]
        self.sub([],nums,lists)
        return lists


    def sub(self,p,up,lists):
        if up==[]:
            lists.append(p)
            return
        self.sub(p+[up[0]],up[1:],lists)
        self.sub(p,up[1:],lists)

