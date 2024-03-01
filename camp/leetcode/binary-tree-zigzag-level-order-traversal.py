# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        def helper(node, level,  dir):
            if not node:
                return
            if len(ans) <=level:
                ans.append([]) #forming new empty list in ans

            if dir ==1:
                ans[level].append(node.val)
            else:
                ans[level].insert(0, node.val)
            
            helper(node.left, level+1, 1-dir)
            helper(node.right, level+1, 1-dir)

        helper(root, 0, 1)
        return ans