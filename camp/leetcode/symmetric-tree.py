# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        s1, s2= root, root

        def helper(s1, s2):
            if s1 ==None and s2==None:
                return True
            if s1==None or s2==None or s1.val != s2.val:
                return False
            
            return helper(s1.left, s2.right) and helper(s1.right, s2.left)
        return helper(s1, s2) 