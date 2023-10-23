class Solution(object):
    def isPalindrome(self, s):
        str=""
        for i in s:
            if i.isalnum():
                str+=i.lower()
            # if i.isnumeric():
            #     str+=i
            # if i.isalpha():
            #     str+=i.lower()
        return str==str[::-1]
