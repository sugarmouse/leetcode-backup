#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#
# @lc code=start
from typing import List, Optional


class Solution:
    def numTrees(self, n: int) -> int:
        self.memo = [[0 for _ in range(n+1)] for _ in range(n+1)]
        return self.numTreesHelper(1, n)

    def numTreesHelper(self, lo: int, hi: int) -> int:

        if lo > hi:
            return 1
        # 缓存命中，直接返回
        if self.memo[lo][hi] != 0:
            return self.memo[lo][hi]

        res = 0
        for i in range(lo, hi+1):
            left = self.numTreesHelper(lo, i-1)
            right = self.numTreesHelper(i+1, hi)
            res += left * right
        # 缓存结果
        self.memo[lo][hi] = res
        return res
# @lc code=end
