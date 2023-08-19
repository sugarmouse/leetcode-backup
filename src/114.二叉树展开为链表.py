#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        right = root.right
        
        if root.left:
            root.right = root.left
            tail = root
            while tail.right:
                tail = tail.right
            tail.right = right
            root.left = None



# @lc code=end

# 遍历节点的思想
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        right = root.right
        
        if root.left:
            root.right = root.left
            tail = root
            while tail.right:
                tail = tail.right
            tail.right = right
            root.left = None