#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        
        root_val = postorder[-1]
        root_index_in = inorder.index(root_val)

        root = TreeNode(root_val)

        inorder_left = inorder[:root_index_in]
        inorder_right = inorder[root_index_in+1:]

        left_size = len(inorder_left)
        postorder_left = postorder[:left_size]
        postorder_right = postorder[left_size: -1]

        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)

        return root
# @lc code=end
