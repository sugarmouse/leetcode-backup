#
# @lc app=leetcode.cn id=654 lang=python3
#
# [654] 最大二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return self.construct(nums, 0, len(nums))

    def construct(self, nums: List[int], left: int, right: int) -> Optional[TreeNode]:
        if left == right:
            return None

        max_num = max(nums[left:right])
        max_index = nums.index(max_num)

        root = TreeNode(val=max_num)

        if max_index > left:
            root.left = self.construct(nums, left, max_index)
        if max_index < right - 1:
            root.right = self.construct(nums, max_index + 1, right)

        return root

# @lc code=end
