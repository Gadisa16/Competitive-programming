class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans, nearest_sum = float(inf), 0
        nums.sort()
        
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]

                if abs(s-target) < ans:
                    ans = abs(s-target)
                    nearest_sum = s

                if s < target:
                    l +=1
                elif s > target:
                    r -=1
                else:
                    return nearest_sum 
        
        return nearest_sum