class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = nums.index(0) if 0 in nums else len(nums)
        
        for j in range(i+1, len(nums)):
            if nums[i] == 0 and nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

        return nums      