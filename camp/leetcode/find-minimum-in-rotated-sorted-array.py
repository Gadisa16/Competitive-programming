class Solution:
    def findMin(self, nums: List[int]) -> int:
    
        l, r =0, len(nums)-1
        while l<= r:
            if nums[l] <= nums[r]: #if non rotated
                return nums[l]

            mid =(l+r)//2

            if nums[mid] >=nums[l]:
                l =mid+1
            else:
                r= mid

        