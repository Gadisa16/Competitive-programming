class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        for val in nums1:
            for val2 in nums2:
                if val ==val2:
                    return val
                if val2 >val:
                    break
        return -1