class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        rate1, rate2 =1, max(piles)

        while rate1 < rate2:
            k = (rate2 + rate1)//2
            curh =0
            for ban in piles:
                curh += ceil(ban/k)
            
            if curh >h: #we have to increase rate (rate1)
                rate1 = k+1
            else: #try to decrease rate (rate2)
                rate2 = k
                
        return rate2




        