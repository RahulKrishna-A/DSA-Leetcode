class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        lists=[]
        self.permutations([],nums,lists)
        return lists


    def permutations(self,p,up,lists):
        if up==[]:
            lists.append(p)
            return
        li = up[0]
        for i in range(len(p)+1):
            s = p[0:i]
            e = p[i:]
            self.permutations(s+[li]+e,up[1:],lists)