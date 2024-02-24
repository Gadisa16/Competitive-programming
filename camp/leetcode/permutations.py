class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:


        def recursive(combination, result):
            
            if len(combination) == len(nums):
                result.append(combination[:])
                return

            for i in range(len(nums)):
                if nums[i] in combination:
                    continue
                combination.append(nums[i])
                recursive(combination, result)
                combination.pop()

        result = []
        recursive([], result)
        return result
        