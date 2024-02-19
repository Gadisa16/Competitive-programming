class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        dep, ans =0, 0
#(( ()() )) (), think interms of depth
        for i in range(len(s)):
            if s[i]== "(":
                dep +=1

            elif s[i]==")":
                if s[i-1]=="(":
                    ans += 2**(dep-1)
                dep -=1
        return ans
                



                
                

        