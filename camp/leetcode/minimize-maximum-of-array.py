class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        max_val, pref = nums[0], 0
        for i in range(len(nums)):
            pref +=nums[i]
            max_val =max(max_val, ceil(pref/(i+1)))
        return max_val

#max_val =max(max_val, ceil(pref/(i+1))) #calculating and comparing z average at every points