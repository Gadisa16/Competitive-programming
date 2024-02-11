class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic= {0:1}
        count, pref=0, 0

        for i in range(len(nums)):
            pref +=nums[i]
            rem= pref%k

            if rem in dic: #check if rem is occured before
                count +=dic[rem]
                dic[rem] +=1
            else:
                dic[rem]=1
        return count

            
            