class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        len1, len2 = len(nums1), len(nums2)
        i, j = 0, 0
        res = []
        while i< len1 and j < len2:
            if nums1[i][0] == nums2[j][0]:
                res.append([nums1[i][0], nums1[i][1]+nums2[j][1]])
                i +=1
                j +=1

            elif nums1[i][0] <= nums2[j][0]:
                res.append(nums1[i])
                i +=1
            else:
                res.append(nums2[j])
                j +=1

        res.extend(nums1[i:] if i < len1 else nums2[j:])
        return res