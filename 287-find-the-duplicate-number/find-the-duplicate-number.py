class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            val = nums[i]
            if val != -1 and val != i+1:
                if nums[val-1] == -1:
                    return val
                nums[i], nums[val-1] = nums[val-1], -1
                
                if nums[i] == -1:
                    i +=1
            else:
                nums[i] = -1
                i +=1