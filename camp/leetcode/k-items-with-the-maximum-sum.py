class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        
        leftP =k -(numOnes +numZeros)
        if leftP <=0: #if all place in k's are allocated by 1 and 0
            return min(k, numOnes)

        return numOnes -leftP #if there is place left from 0 & 1, we have to put -1 inorder to fill the bag
        
        
        
        


        