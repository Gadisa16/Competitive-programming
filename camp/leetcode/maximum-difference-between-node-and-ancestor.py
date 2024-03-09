# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        minVal, maxVal= root.val, root.val
        maxDiff =maxVal-minVal
        def helper(root, mn, mx, mxd):
            if not root:
                return mxd
            
            mn= min(mn, root.val)
            mx= max(mx, root.val)
            mxd =max(mxd, mx-mn)
            mxd= helper(root.left, mn, mx, mxd)
            mxd= helper(root.right, mn, mx, mxd)
            return mxd
        res =helper(root, minVal, maxVal, maxDiff)
        return res