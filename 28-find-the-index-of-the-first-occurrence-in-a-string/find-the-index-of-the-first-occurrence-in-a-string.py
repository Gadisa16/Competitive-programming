class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h_len, n_len = len(haystack), len(needle)

        if n_len > h_len: return -1

        l = 0
        for r in range(n_len-1, h_len):
            if needle == haystack[l:r+1]:
                return l
            l +=1
            r +=1
        return -1