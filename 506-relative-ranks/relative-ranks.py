class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        hp = [] #heap

        for i, val in enumerate(score):
            heapq.heappush(hp, (-val, i))
        
        rank = 1
        while hp:
            ind = heapq.heappop(hp)[1]

            if rank == 1:
                score[ind] = "Gold Medal"
            elif rank == 2:
                score[ind] = "Silver Medal"
            elif rank == 3:
                score[ind] = "Bronze Medal"
            else:
                score[ind] = str(rank)

            rank +=1   
        return score