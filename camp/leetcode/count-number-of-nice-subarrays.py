class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums= [1 if val%2!=0 else 0 for val in nums]
        dic = {0:1}
        prefSum, count = 0, 0
        for val in nums:
            prefSum += val

            if prefSum -k in dic:
                count += dic[prefSum-k]
            
            dic[prefSum] = dic.get(prefSum, 0) +1
        return count

