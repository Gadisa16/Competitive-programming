class Solution:
    def breakPalindrome(self, palind: str) -> str:
        if len(palind)==1:
            return ""
        for i in range(len(palind)//2):
            if palind[i] !="a":
                return palind[:i] +"a" + palind[i+1:]
        
        return palind[:-1] + "b"
            
        