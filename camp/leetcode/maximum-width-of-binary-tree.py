# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans =0
        q = deque([[root, 1, 0]]) #[node, assigned_num, level]
        leftMostNum, leftMostNumLevel = 1, 0 #changed when level updated

        while q:
            curNode, num, level = q.popleft()

            if level >leftMostNumLevel: #i.e we reached new level
                leftMostNumLevel =level
                leftMostNum =num
            ans =max(ans, num- leftMostNum +1)

            if curNode.left:
                q.append([curNode.left, 2*num, level+1])
            if curNode.right:
                q.append([curNode.right, 2*num+1, level+1])
        return ans