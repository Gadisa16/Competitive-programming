class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        
        mod= [0]*(n+1)
        for i, j, k in bookings:
            mod[i-1] +=k    
            mod[j] -=k

        for i in range(1, len(mod)):
            mod[i] +=mod[i-1]
        
        mod.pop()
        return mod


        