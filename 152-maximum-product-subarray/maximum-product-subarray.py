class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float("-inf")
        cur_max = cur_min = 1

        for n in nums:
            temp = cur_min * n

            cur_min = min(cur_max*n, cur_min * n, n)
            cur_max = max(cur_max*n, temp, n)

            res = max(res, cur_max)
        
        return res