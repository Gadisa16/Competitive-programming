class Solution:
    def splitString(self, s: str) -> bool:
        def dfs(prev, indx):
            if indx==len(s):
                return True

            for j in range(indx, len(s)):
                curv =int(s[indx: j+1])
                if curv- prev==-1 and dfs(curv, j+1):
                    return True
            return False
        
        for i in range(len(s)-1):
            val =int(s[:i+1])
            if dfs(val, i+1): return True
        return False