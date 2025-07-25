class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic = {}
        s = [word for word in s.split()]
        if len(pattern) != len(s):
            return False
        
        for i, word in enumerate(s):
            ch = pattern[i]
            if ch not in dic:
                if word in dic.values():
                    return False
                dic[ch] = word
            else:
                if dic[ch] != word:
                    return False
        return True
