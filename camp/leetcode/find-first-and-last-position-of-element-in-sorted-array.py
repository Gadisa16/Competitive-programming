class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) ==0:
            return [-1, -1]
        
        def leftMost(target):
            l, r = 0, len(nums)-1
            while l < r: #to get left most
                mid = (r+l)//2

                if nums[mid] >= target:
                    r =mid
                else:
                    l = mid + 1
            return r if nums[r]== target else -1
        
        
        def rightMost(target):
            l, r = 0, len(nums)-1
            while l < r: #to get right most
                mid = int(ceil( (l+r)/2 ))

                if nums[mid] <= target:
                    l =mid
                else:
                    r = mid - 1
            return l if nums[l]== target else -1
        
        return [leftMost(target), rightMost(target)]



            
        