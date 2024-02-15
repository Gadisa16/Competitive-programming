class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        arrow, prevEnd =1, points[0][1]

        for curStart, curEnd in points[1:]:
            if prevEnd < curStart:
                arrow +=1
                prevEnd= curEnd
            elif prevEnd >= curStart:
                prevEnd= min(prevEnd, curEnd)
        return arrow