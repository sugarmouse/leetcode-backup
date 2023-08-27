#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        self.memo = [[None for _ in range(n+1)] for _ in range(n + 1)]
        return self.buildTree(1, n)

    def buildTree(self, lo: int, hi: int) -> List[Optional[TreeNode]]:
        if lo > hi:
            return [None]

        if self.memo[lo][hi] is not None:
            return self.memo[lo][hi]

        res = []
        for mid in range(lo, hi + 1):
            left = self.buildTree(lo, mid - 1)
            right = self.buildTree(mid + 1, hi)

            for leftTree in left:
                for rightTree in right:
                    root = TreeNode(mid)
                    root.left = leftTree
                    root.right = rightTree
                    res.append(root)
        # 作缓存
        self.memo[lo][hi] = res
        return res


# @lc code=end
