class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        r, count= len(nums)-1, 0
    
        while r >= 2:
            i, j = 0, r-1
            while i<j:
                if nums[i] +nums[j] > nums[r]:
                    count += j-i
                    j -=1
                else:
                    i +=1
            r -=1
        return count