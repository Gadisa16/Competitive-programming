class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        dic ={0:1}
        count, pref =0, 0

        for i in range(len(nums)):
            pref +=nums[i]
            
            if pref- goal in dic:
                count += dic[pref- goal]
           
            dic[pref] = dic.get(pref,0)+1

        return count

                
            
