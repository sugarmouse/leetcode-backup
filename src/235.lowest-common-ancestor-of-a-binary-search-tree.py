#
# @lc app=leetcode.cn id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        min_val, max_val = min(p.val, q.val), max(p.val, q.val)
        return self.find(root, min_val, max_val)

    def find(self, node: 'TreeNode', min_val: int, max_val: int) -> 'TreeNode':
        if node is None:
            return None
        if node.val < min_val:
            return self.find(node.right, min_val, max_val)
        if node.val > max_val:
            return self.find(node.left, min_val, max_val)
        return node
# @lc code=end
