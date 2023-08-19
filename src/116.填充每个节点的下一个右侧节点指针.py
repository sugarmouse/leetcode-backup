#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# 遍历节点的思路
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return

        self.traverse(root.left, root.right)
        return root

    def traverse(self, node1: 'Optional[Node]', node2: 'Optional[Node]') -> None:
        if node1 is None or node2 is None:
            return

        node1.next = node2

        self.traverse(node1.left, node1.right)
        self.traverse(node2.left, node2.right)
        self.traverse(node1.right, node2.left)


# @lc code=end


# 分解子问题
class Solution1:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return

        left = self.connect(root.left)
        right = self.connect(root.right)

        while left and right:
            left.next = right
            left = left.right
            right = right.left

        return root
