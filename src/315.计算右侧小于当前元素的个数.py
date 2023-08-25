#
# @lc app=leetcode.cn id=315 lang=python3
#
# [315] 计算右侧小于当前元素的个数
#

# @lc code=start


# 利用归并排序的过程中，不断地寻找左边的数组中每个元素在右边数组中比自己小的元素的个数
# 而归并排序最终的叶子节点都是单个元素，所以这里会找全，
# 而 左右子数组的划分，右使得找到的符合要求的元素不会重复
from typing import NamedTuple


class Pair(NamedTuple):
    val: int
    id: int


class Solution:
    def __init__(self):
        self.count = []
        self.temp = []

    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        self.count = [0 for _ in range(n)]
        self.temp = [Pair(0, 0) for _ in range(n)]
        arr: List[Pair] = [Pair(val, i) for i, val in enumerate(nums)]

        self.sort(arr, 0, n - 1)
        return self.count

    def sort(self, arr: List[Pair], lo: int, hi: int):
        if lo == hi:
            return
        mid = (lo + hi) // 2

        self.sort(arr, lo, mid)
        self.sort(arr, mid + 1, hi)
        self.merge(arr, lo, mid, hi)

    def merge(self, arr: List[Pair], lo: int, mid: int, hi: int):

        for i in range(lo, hi + 1):
            self.temp[i] = arr[i]

        i, j = lo, mid + 1
        p = lo
        while p <= hi:
            if i > mid:
                arr[p] = self.temp[j]
                j += 1
            elif j > hi:
                arr[p] = self.temp[i]
                i += 1
                self.count[arr[p].id] += j - mid - 1
            elif self.temp[i].val > self.temp[j].val:
                arr[p] = self.temp[j]
                j += 1
            else:
                arr[p] = self.temp[i]
                i += 1
                self.count[arr[p].id] += j - mid - 1

            p += 1

# @lc code=end
