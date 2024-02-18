class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        dic = {}
        stack= []

        for great_n in nums2:
            while stack and great_n > stack[-1]:
                prev_val= stack.pop()
                dic[prev_val] = great_n

            stack.append(great_n)

        return [dic.get(n1, -1) for n1 in nums1]

        