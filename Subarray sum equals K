class Solution(object):
    def subarraySum(self, nums, k):
        count = 0
        prefix_sum = 0
        sum_count = {0: 1}  # A dictionary to keep track of the count of prefix sums
        
        for num in nums:
            prefix_sum += num
            if (prefix_sum - k) in sum_count:
                count += sum_count[prefix_sum - k]
            if prefix_sum in sum_count:
                sum_count[prefix_sum] += 1
            else:
                sum_count[prefix_sum] = 1
        
        return count
