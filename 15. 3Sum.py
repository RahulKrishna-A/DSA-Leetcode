class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        j = i+1
        k = len(nums)-1
        ans = []
        nums.sort()
        for i in range(len(nums)):
            if i!=0 and nums[i-1]==nums[i]:
                continue
            j=i+1
            k=len(nums)-1
            while j<k:
                sums = nums[i]+nums[k]+nums[j]
                if sums>0:
                    k-=1
                elif sums<0:
                    j+=1
                else:
                    ans.append([nums[i],nums[j],nums[k]])
                    j+=1
                    while nums[j-1]==nums[j] and  j<k:
                        j+=1
        return ans




