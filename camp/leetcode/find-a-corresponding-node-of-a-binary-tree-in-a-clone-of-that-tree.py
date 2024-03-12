# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        q = [cloned]

        while q:
            node = q.pop()
            if node.val == target.val:
                return node
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
