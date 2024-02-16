class Solution(object):
    def isValid(self, s):
        stack=[]
        pairs={
            '[': ']',
            '(': ')',
            '{': '}'
        }
        for br in s:
            if br in pairs:
                stack.append(br)
            elif len(stack) == 0 or br != pairs[stack.pop()]:
                return False
        return len(stack)==0

""" line 9 & 10: if bracket given in string is in pairs as key (open bracket)""" 
"""line 12: if stack is empty(no open bracket existed) or the last value added to stack is not value pair of first closed bracket
"""  
"""line 14: at the end of program(for loop) if all the bracket in stack is popped to its equivalent value pair and no key pair(no open br is left) then return true """
        