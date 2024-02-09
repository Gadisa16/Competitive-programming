class Solution:
    def maxScore(self, s: str) -> int:
        leng, maxs, cur= len(s), 0, 0

        for j in range(1, leng):
            cur= s[:j].count("0") + s[j:].count("1")
            maxs= max(maxs, cur)
        return maxs