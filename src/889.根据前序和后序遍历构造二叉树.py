#
# @lc app=leetcode.cn id=889 lang=python3
#
# [889] 根据前序和后序遍历构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])


        root_val = preorder[0]
        root = TreeNode(root_val)
        left_root_val = preorder[1]
        left_root_index_post = postorder.index(left_root_val)

        post_left = postorder[:left_root_index_post + 1]
        post_right = postorder[left_root_index_post+1: -1]

        left_size = len(post_left)

        pre_left = preorder[1:left_size+1]
        pre_right = preorder[left_size+1:]

        root.left = self.constructFromPrePost(pre_left, post_left)
        root.right = self.constructFromPrePost(pre_right, post_right)

        return root
        
# @lc code=end

