class Solution:
    def helper(self,s,prev,idx):
        if(idx == len(s) and prev != s ):
            return True 
        c = ""
        for i in range(idx,len(s)):
            c += s[i]
            if(prev != ""):
                if(int(prev) - int(c) == 1 ):
                    if(self.helper(s,c,i+1)): 
                        return True 
            else:
                if(self.helper(s,c,i+1)):
                    return True 
        return False 
        
    def splitString(self, s: str) -> bool:   
        return self.helper(s,"",0)