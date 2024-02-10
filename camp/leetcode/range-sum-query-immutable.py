class NumArray(object):

    def __init__(self, nums):
        self.pref_sum= [0]*(len(nums)+1)
        for i in range(len(nums)):
            self.pref_sum[i]= self.pref_sum[i-1] + nums[i]   

    def sumRange(self, left, right):
        l_r= self.pref_sum[right]-self.pref_sum[left-1]
        return l_r


"""
pref_sum[i-1], since pref_sum sum is initialised to 0 pref_sum[i-1] when i==0 is same with pref_sum[-1] which is elt at top and since all elts are Zero elt at top is also Zero
"""
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)