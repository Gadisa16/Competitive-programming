class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        i, count = len(nums)-2, 0
        while i>=0:
            space= 0
            if nums[i] >nums[i+1]:
                space= ceil(nums[i]/nums[i+1])
                nums[i]= nums[i]//space
                count +=space-1
            i -=1
        return count       