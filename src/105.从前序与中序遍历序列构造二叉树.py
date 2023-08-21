#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)
        root_index_in = inorder.index(root_val)

        # 分割左右 inorder
        left_inorder = inorder[:root_index_in]
        right_inorder = inorder[root_index_in+1:]

        # 分割左右 preoder
        left_preorder = preorder[1:len(left_inorder)+1]
        right_preorder = preorder[len(left_preorder) + 1:]

        # 递归的构建左右子树
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)

        return root
# @lc code=end
