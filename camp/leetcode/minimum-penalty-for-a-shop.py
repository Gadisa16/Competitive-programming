class Solution:
    def bestClosingTime(self, customers: str) -> int:
        arr=[]
        penality = float("inf")
        index = -1
        for letter in customers:
            if letter == "Y":
                arr.append(1)
            else:
                arr.append(0)
        arr = list(accumulate(arr))
        for i in range(len(arr)):
            if i == 0:
                p = arr[-1]
            if i > 0:
                before = i - arr[i-1]
                after = arr[-1] - arr[i-1]
                p = before+after
            if p < penality:
                penality = p
                index = i
        last_pen = len(arr) - arr[-1]
        if last_pen < penality:
            penality = last_pen
            index = len(arr)
        return index 
