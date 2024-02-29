class Solution(object):
    def partitionLabels(self, s):
        lastCharIdx={}
        res=[]
        size, end= 0, 0

        for i, char in enumerate(s):
            lastCharIdx[char]= i #{'a':8, b:5}
        
        for i, char in enumerate(s):
            end= max(end, lastCharIdx[char]) #8 for first iteration
            size+=1

            if i==end: #for first iteration i=0, end=8 -> not equal
               res.append(size)
               size=0
        return res


        