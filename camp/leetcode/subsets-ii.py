class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans =[]
        nums.sort()
        
        def backtrack(ind, subset):
            ans.append(subset[:])

            for i in range(ind, len(nums)):
                if i >ind and nums[i-1] ==nums[i]:
                    continue
                subset.append(nums[i])
                backtrack(i+1, subset)
                subset.pop()

        backtrack(0, [])
        return ans
        