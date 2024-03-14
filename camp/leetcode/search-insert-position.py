class Solution(object):
    def searchInsert(self, nums, target):
        l, r = 0, len(nums)-1
        while l <= r:
            mid_idx = (l+r)//2

            if nums[mid_idx] ==target:
                return mid_idx
            elif target > nums[mid_idx]:
                l =mid_idx +1
            else:
                r =mid_idx -1
        return l #for target not in nums, if l==r and target>nums[mid] we insert at l+1, but if target< nums[r]: we insert exactly at l index and the other elts are shifted

        