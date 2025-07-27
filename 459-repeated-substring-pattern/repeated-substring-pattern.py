class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        leng = len(s)
        for r in range(1, leng//2 +1):
            if leng % r == 0: # consider r as substring length 
                if s[:r]*(leng//r) == s:
                    return True
        return False