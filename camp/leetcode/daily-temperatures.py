class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack=[]
        ans=[0]*len(temp)
        #this is called monotonically decreasing stack
        for i, Tval in enumerate(temp):
            while stack and Tval > stack[-1][1]:
                prev_ind, prev_temp = stack.pop()
                ans[prev_ind] = i- prev_ind #i is our current index

            stack.append([i, Tval])
        return ans
        