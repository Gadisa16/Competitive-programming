class Solution:
    def minOperations(self, nums: List[int]) -> int:
        oper =0
        for i in range(1, len(nums)):
            if nums[i-1] >=nums[i]:
                add = nums[i-1] -nums[i] +1
                nums[i] +=add
                oper += add
    
        return oper

        