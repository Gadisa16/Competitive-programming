class Solution(object):
    def minSubArrayLen(self, target, nums):
        l, r = 0, 0
        min_len = len(nums)+1
        sum=0
        for r in range(len(nums)):
            sum+=nums[r]

            while sum>=target: #don't use if here
                min_len= min(min_len, r-l+1) #not r-l+1, coz we have already inceased r by 1 (r+=1)
                sum-=nums[l]
                l+=1

        if min_len>len(nums):
            return 0
        else:
            return min_len

"""min_len=len(nums)+1 Using len(nums) as the initial value might lead to incorrect results or difficulties in distinguishing between an initial value and valid subarray lengths. so using min_len>len(nums) is must"""  
       
                








        
        