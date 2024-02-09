class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        mod=[0]*1001
        for pas, fro, to in trips:
            mod[fro] +=pas
            mod[to] -=pas
        
        for i in range(1, len(mod)):
            mod[i] +=mod[i-1]

        return max(mod)<=capacity



        