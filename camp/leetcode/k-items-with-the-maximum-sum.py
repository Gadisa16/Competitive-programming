class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        
        leftP =k -(numOnes +numZeros)
        if leftP <=0:
            return min(k, numOnes)

        return numOnes -leftP
        
        
        
        


        