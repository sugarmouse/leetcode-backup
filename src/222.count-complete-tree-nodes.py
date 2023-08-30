#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 一颗完全二叉树的两颗子树，至少有一颗是满二叉树
# O(logN*logN)
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        left, right = root, root
        sz_l = sz_r = 0

        while left:
            left = left.left
            sz_l += 1

        while right:
            right = right.right

        if sz_l == sz_r:
            return 2 ** sz_r - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

# @lc code=end
