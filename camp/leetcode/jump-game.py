class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach, leng =0, len(nums)
        if leng==1:
            return True
            
        for i in range(leng):
            if maxReach <i:
                return False
            
            maxReach= max(maxReach, nums[i]+i)
            if maxReach >=leng-1:
                return True