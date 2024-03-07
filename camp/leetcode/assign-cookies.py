class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count =0
        for i in range(len(g)-1, -1, -1):
            if not s:
                break
            if g[i] <= s[-1]:
                count +=1
                s.pop()
        return count
        