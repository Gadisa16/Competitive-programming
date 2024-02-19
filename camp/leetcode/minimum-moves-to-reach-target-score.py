class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans =0
        while target >1:
            if maxDoubles:
                ans += ceil((target/2)- (target//2)) +1
                maxDoubles -=1
                target= target//2
               
            else:
                ans += target-1
                return ans
        return ans
        