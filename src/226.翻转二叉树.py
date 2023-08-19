#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 前序遍历
class Solution:

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.traverse(root)
        return root

    def traverse(self, root: Optional[TreeNode]):
        if root is None:
            return
        root.left, root.right = root.right, root.left
        self.traverse(root.left)
        self.traverse(root.right)


# @lc code=end


# 子问题分解思路
class Solution2:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        root.left,  root.right = self.invertTree(
            root.right), self.invertTree(root.left)
        return root

# 中序遍历
class Solution2:

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.traverse(root)
        return root

    def traverse(self, root: Optional[TreeNode]):
        if root is None:
            return
        self.traverse(root.left)
        root.left, root.right = root.right, root.left
        self.traverse(root.left)