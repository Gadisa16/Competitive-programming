# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        invert = root
        invert.left, invert.right = invert.right, invert.left

        self.invertTree(invert.left)
        self.invertTree(invert.right)

        return invert