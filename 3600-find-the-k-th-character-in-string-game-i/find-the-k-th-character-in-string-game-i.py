class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        while len(word) < k:
            temp = ""
            for ch in word:
                # temp += chr(97 + ((ord(ch)-97)+1)%26)
                asc = ord(ch) + 1 if ch != "z" else ord(ch)
                temp += chr(asc)
            word += temp
     
        return word[k-1]