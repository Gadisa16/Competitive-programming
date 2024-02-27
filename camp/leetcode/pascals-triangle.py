class Solution:
    def generate(self, nR: int) -> List[List[int]]:
        if nR ==1:
            return [[1]]
        Triangle = self.generate(nR-1)

        prevR =Triangle[-1]
        curR =[1] #every row starts and end by 1, this is start
        for c in range(1, len(prevR)): #for values b/n left's and right's 1
            curR.append(prevR[c-1] +prevR[c])
        curR.append(1) #this 1 at end
        Triangle.append(curR)

        return Triangle

