class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans, subset = [], []
       
        def backtrack(i):
            if i >= len(nums):
                ans.append(subset[:])
                return
                
            #decision to include nums[i]
            subset.append(nums[i])
            backtrack(i + 1)

            #decision not to include nums[i]
            subset.pop()
            backtrack(i + 1)

        backtrack(0)
        return ans