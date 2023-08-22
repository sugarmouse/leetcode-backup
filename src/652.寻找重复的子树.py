#
# @lc app=leetcode.cn id=652 lang=python3
#
# [652] 寻找重复的子树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:

    def __init__(self) -> None:
        self.map = {}
        self.res = []

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.serialize(root)
        return self.res

    def serialize(self, node: Optional[TreeNode]) -> str:
        if node is None:
            return '#'

        left = self.serialize(node.left)
        right = self.serialize(node.right)

        str_me = f'{left},{right},{node.val}'

        if str_me in self.map:
            # 说明有重复当前节点的子树
            if self.map[str_me] == 1:
                self.res.append(node)
            self.map[str_me] += 1
        else:
            self.map[str_me] = 1

        return str_me


# @lc code=end
