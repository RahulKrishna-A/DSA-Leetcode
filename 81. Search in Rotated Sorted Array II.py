class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        s=0
        e=len(nums)-1
        while s<=e:
            mid = s+(e-s)//2
            if nums[mid]==target:
                return True
            if nums[mid]==nums[s] and nums[mid]==nums[e]:
                s+=1
                e-=1
                continue
            if nums[mid]>=nums[s]:
                if target<nums[mid] and target>=nums[s]:
                    e=mid-1
                else:
                    s=mid+1
            else:
                if target>nums[mid] and target<=nums[e]:
                    s=mid+1
                else:
                    e=mid-1
        return False
