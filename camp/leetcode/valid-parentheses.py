class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for br in s:
            if br in "[{(":
                stack.append(br)

            elif not stack or stack[-1]== "(" and br !=")" or stack[-1]== "{" and br !="}" or stack[-1]== "[" and br !="]":
                return False
                
            else:
                stack.pop()

        return len(stack) == 0

        