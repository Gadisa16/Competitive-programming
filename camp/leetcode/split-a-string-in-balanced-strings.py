class Solution:
    def balancedStringSplit(self, s: str) -> int:
        i, bal =0, 0
        for st in s:
            if st=="R":
                i +=1
            else:
                i -=1
            bal +=1 if i==0 else 0
        return bal
            
        

        