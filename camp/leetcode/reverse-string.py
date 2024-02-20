class Solution(object):
    def reverseString(self, s):
        s[:]= s[::-1]


"""
:type s: List[str]
:rtype: None Do not return anything, modify s in-place instead.
 
 
 what is difference between s=s[::-1] and s[:]=s[::-1] if s is python list?
 The difference lies in how the original list s is modified. s = s[::-1]: This line creates a reversed copy of the list s and assigns it to the variable s. It doesn't modify the original list; instead, it creates a new list with the reversed elements and assigns it to the same variable s. If s was referencing something else before, it now references the new reversed list. 
 
s[:] = s[::-1]: This line modifies the original list s by replacing its contents with the reversed elements of s. It uses list slicing ([:]) to access the entire list and replaces its elements with the reversed elements of the same list. This operation directly modifies the existing list s rather than creating a new list or changing what s references.
 """
      
        