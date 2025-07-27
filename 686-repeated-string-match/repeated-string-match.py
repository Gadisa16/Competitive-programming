class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if b in a:
            return 1
        
        c = b.count(a)

        for i in range(c, c+3):
            if b in a*i:
                return i
        return -1