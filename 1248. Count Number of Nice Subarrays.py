class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        pref ={}
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[i]=0
            else:
                nums[i]=1
        answer=0
        curr_sum=0
        for i in range(len(nums)):
            curr_sum+=nums[i]
            if curr_sum==k:
                answer+=1
            if curr_sum-k in pref and curr_sum>=k:
                answer+=pref[curr_sum-k]
            pref[curr_sum]= pref.get(curr_sum,0)+1
        return answer
