class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        mod, leng= 10**9 +7, len(nums)
        req, ans= [0]*leng, 0

        for start, end in requests:
            req[start] +=1
            if end < leng-1:
                req[end+1] -=1
        
        for i in range(1, leng):
            req[i] += req[i-1]
        
        req.sort()
        nums.sort()
        for i in range(leng):
            ans += req[i]* nums[i]
        return ans%mod

        
        