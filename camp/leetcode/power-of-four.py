class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n== 1:
            return 1
        
        if n<= 0 or n%4 !=0:
            return False
        
        return self.isPowerOfFour(n/4)
        