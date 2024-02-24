class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        sec, leng =0, len(tickets)
        minn , i=min(tickets), 0
        while i<leng:
            if tickets[i] !=0:
                tickets[i] -=1
                sec += 1
            if tickets[k] ==0:
                return sec
            i =(i+1)%leng
