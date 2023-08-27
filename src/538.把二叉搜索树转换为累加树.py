#
# @lc app=leetcode.cn id=538 lang=python3
#
# [538] 把二叉搜索树转换为累加树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.sum = 0
        self.traverse(root)
        return root

    def traverse(self, node: Optional[TreeNode]):
        if node is None:
            return
        self.traverse(node.right)
        self.sum += node.val
        node.val = self.sum
        self.traverse(node.left)
# @lc code=end
