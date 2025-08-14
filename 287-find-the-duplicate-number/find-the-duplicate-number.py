class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s, f = 0, 0 # slow and fast pointer
        
        while True:
            s = nums[s]
            f = nums[nums[f]]

            if s == f:
                break
        
        s2 = 0 # resetted s
        while True:
            s2 = nums[s2]
            s = nums[s]
            if s2 == s:
                return s