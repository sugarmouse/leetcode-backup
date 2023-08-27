#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.res = 0
        self.k = k
        self.traverse(root)
        return self.res
    
    def traverse(self, node:Optional[TreeNode]):
        if node is None:
            return
        self.traverse(node.left)
        self.count += 1
        if self.count == self.k:
            self.res = node.val
        self.traverse(node.right)
# @lc code=end

