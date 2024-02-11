class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_pro=[1]
        for i in range(1, len(nums)):
            l_pro.append(l_pro[i-1]*nums[i-1])
        
        r_pro=[1]
        for i in range(len(nums)-2, -1, -1):
            r_pro.insert(0,r_pro[0]*nums[i+1]) 
        
        return[l_pro[i] *r_pro[i] for i in range(len(nums))]

        