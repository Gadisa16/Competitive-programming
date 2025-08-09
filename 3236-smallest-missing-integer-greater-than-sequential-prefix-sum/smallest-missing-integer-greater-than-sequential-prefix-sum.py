class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        ssum = nums[0]

        for j in range(1, len(nums)):
            if nums[j] - nums[j-1] == 1:
                ssum += nums[j] 
            else: 
                break
        
        while ssum in nums:
            ssum += 1
        
        return ssum