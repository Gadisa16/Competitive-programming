# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        maxc, dic = 0, defaultdict(int)

        def func(node):
            nonlocal maxc
            if not node:
                return 0
            dic[node.val] += 1

            func(node.left)
            func(node.right)

            maxc = max(maxc, dic[node.val])  # Update maxc
            return

        func(root)

        return [k for k, v in dic.items() if v == maxc]
