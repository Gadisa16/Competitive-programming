class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        monStack = []
        res = [-1] * len(nums)
        for _ in range(2):
            for i in range(len(nums)):
                while monStack and nums[i] > nums[monStack[-1]]:
                    res[monStack.pop()] = nums[i]
                monStack.append(i)
        return res
            