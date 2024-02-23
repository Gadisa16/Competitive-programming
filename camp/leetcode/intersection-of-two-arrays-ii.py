class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1, count2 =Counter(nums1), Counter(nums2)
        ans = ""
        for val in count1:
            ans +=(str(val) +" ")*min(count1[val], count2[val])
        
        return list(map(int, ans.split()))
                

        