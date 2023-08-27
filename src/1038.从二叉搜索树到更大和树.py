#
# @lc app=leetcode.cn id=1038 lang=python3
#
# [1038] 从二叉搜索树到更大和树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 利用 BST 的中旬遍历有序的性质
    # 而不需要真的一个节点一个节点的去比较大小
    def bstToGst(self, root: TreeNode) -> TreeNode:
        cur_sum = 0

        def traverse(node:Optional[TreeNode]):
            nonlocal cur_sum
            if node is None:
                return
            traverse(node.right)
            cur_sum += node.val
            node.val = cur_sum
            traverse(node.left)

        traverse(root)
        return root

# @lc code=end

