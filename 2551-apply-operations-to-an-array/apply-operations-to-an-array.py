class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        arr, leng = [], len(nums)   
        l, r = 0, 1
        while r < leng:
            if nums[l] == nums[r]:
                nums[l] *=2
                nums[r] = 0

            if nums[l] != 0:
                arr.append(nums[l])

            l +=1
            r +=1

        return arr + [nums[leng-1]] + [0]*(leng-len(arr)-1)