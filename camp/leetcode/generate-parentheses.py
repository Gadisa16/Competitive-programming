class Solution(object):
    def generateParenthesis(self, n):
        result = []
        def recursion(lc, rc, par):
            
            if lc == rc == n:
                result.append(par)
                return
            
            if lc < n:
                recursion(lc + 1, rc, par+'(')
                
            if lc > rc:
                recursion(lc, rc + 1, par+')')      
            
        recursion(0, 0, '')
        return result