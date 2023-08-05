#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self) -> None:
        self.maxDiameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.findMaxDepth(root)
        return self.maxDiameter

    def findMaxDepth(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        left = self.findMaxDepth(node.left)
        right = self.findMaxDepth(node.right)
        # 更新最大直径
        self.maxDiameter = max(self.maxDiameter, left + right)
        # 返回最大深度
        return max(left, right) + 1


# @lc code=end
