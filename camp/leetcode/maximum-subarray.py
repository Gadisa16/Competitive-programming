class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pref, maxx =0, float("-inf")
        for r in range(len(nums)):
            pref +=nums[r]
            maxx= max(maxx, pref)
            if pref < 0:
                pref =0
                   
        return maxx


        
        









        