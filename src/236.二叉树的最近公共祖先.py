#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 问题转换为两种情况：
#   1. 找一个节点，以该节点为根节点的子树，能在其左右子树中分别找到 p 和 q
#   2. 只在当前节点的一边找到 p 或 q 节点，那么该节点就是两者的 LCA 节点
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None

        if root is q or root is p:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            # 在当前节点的左边和右边都找到了 p 或 q
            # 由于 p q 都存在于树内，且独一无二，所以只能是左子树一个，右子树一个
            # 那么当前节点就是 LCA 节点
            return root
        else:
            # 只在一边找到了目标节点，那么该目标节点就是 LCA 节点
            return left if left else right


# @lc code=end
