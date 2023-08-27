#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isTreeInRange(root, None, None)

    def isTreeInRange(self, node: Optional[TreeNode], min_node: Optional[TreeNode], max_node: Optional[TreeNode]) -> bool:
        """
        检查以 node 为根节点的子树每一个节点的节点值是不是都在 (mid_node.val, max_node.val) 之间
        """
        if node is None:
            return True

        if min_node and node.val <= min_node.val:
            return False
        if max_node and node.val >= max_node.val:
            return False

        isLeft = self.isTreeInRange(node.left, min_node, node)
        isRight = self.isTreeInRange(node.right, node, max_node)

        return isLeft and isRight
# @lc code=end

# 利用中序遍历，记住上一个节点的值，与当前节点比较，
# 出现前一个节点的值不小于当前节点的值，则结果为 false
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.preval = float('-inf')
        self.res = True
        self.traverse(root)
        return self.res

    def traverse(self, node: Optional[TreeNode]):
        if node is None:
            return
        if self.res == False:
            return
        self.traverse(node.left)
        if self.preval >= node.val:
            self.res = False
        self.preval = node.val
        self.traverse(node.right)
