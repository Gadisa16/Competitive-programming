class Solution(object):
    def plusOne(self, digits):
        st= "".join(map(str, digits))
        val= int(st)+1

        return [int(el) for el in str(val)]

        
        