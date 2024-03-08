class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr.append(0)
        stack = []
        i = 0
        result = 0
        while i < len(arr):
            current = arr[i]
            countPrev = 1
            while stack and current <= stack[-1][0]:
                topNum, topCountPrev = stack.pop()
                result += topNum * topCountPrev * countPrev
                countPrev += topCountPrev
            stack.append((current, countPrev))
            i += 1
        return result % (10 ** 9 + 7)