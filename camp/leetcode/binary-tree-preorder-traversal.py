# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans= []
        def pre(root):
            if root:
                ans.append(root.val)
            if root and root.left:
                pre(root.left)
            if root and root.right:
                pre(root.right)
        
        pre(root)
        return ans
            
        


    