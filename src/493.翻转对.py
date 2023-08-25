#
# @lc app=leetcode.cn id=493 lang=python3
#
# [493] 翻转对
#
from typing import List
# @lc code=start
from bisect import bisect_left


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        unique_list = sorted(list(set(nums)))
        map = {}

        # 对原数组 nums 离散化
        for index, val in enumerate(unique_list):
            map[val] = index + 1

        res = 0

        # 树状数组记录每个每个元素 nums[i] 的个数
        bit = BIT(len(map))

        for i in nums:
            bit.add(map[i], 1)
        
        # 因为按顺序遍历的 nums, 满足 i < j 的要求
        for num in nums:
            # 取出当前元素
            bit.add(map[num], -1)
            """ 
            找出 nums 数组中出现过的元素中，可能与当前元素组成
            比如 nums = [1,3,2,3,1]
            unique_list = [1,2,3]
            当前元素 num = nums[1] = 3
            则 t = 1, 说明只有元素 1 可能与 3 组成逆序对
            """
            t = bisect_left(unique_list, num / 2)
            # 更新结果
            res += bit.query(t)

        return res


class BIT:

    def __init__(self, size: int):
        self.size = size
        self.tree = [0 for _ in range(size + 1)]

    def add(self, x: int, k: int):
        i = x
        while i <= self.size:
            self.tree[i] += k
            i = BIT.getParent(i)

    def query(self, x: int):
        res = 0
        i = x
        while i > 0:
            res += self.tree[i]
            i = self.getChild(i)
        return res

    @staticmethod
    def getChild(x: int) -> int:
        return x - BIT.lowbit(x)

    @staticmethod
    def getParent(x: int) -> int:
        return x + BIT.lowbit(x)

    @staticmethod
    def lowbit(x: int):
        return x & -x

# @lc code=end

# 利用 megersort 的特性
# 重点在 merge 两个已经排好序的子数组之前寻找符合要求的翻转对并且更新结果


class Solution2:
    temp_arr = []
    res = 0

    def reversePairs(self, nums: List[int]) -> int:
        sz = len(nums)
        self.temp_arr = [0 for _ in range(sz)]
        self.res = 0
        self.mergeSort(nums, 0, sz - 1)
        return self.res

    def mergeSort(self, arr: List[int], lo: int, hi: int):
        if lo >= hi:
            return

        mid = (lo + hi) // 2
        self.mergeSort(arr, lo, mid)
        self.mergeSort(arr, mid + 1, hi)
        self.merge(arr, lo, mid, hi)

    def merge(self, arr: List[int], lo: int, mid: int, hi: int):

        for index in range(lo, hi + 1):
            self.temp_arr[index] = arr[index]

        # 在合并左右两个数组之前
        # 此时的左右两部分数组分别是排好序的
        # 如果 nums[i] > 2*nums[j] 满足，那么 nums[i+1] > 2*nums[j] 也必定满足（i,j都在合理的范围）
        # 所以这里可以维护一个 end 指针，对于当前左边数组 nums[i], 在区间 [mid + 1, end) 的元素都满足翻转对
        end = mid + 1
        for i in range(lo, mid+1):
            while end <= hi and arr[i] > arr[end] * 2:
                end += 1
            self.res += end - (mid + 1)

        # 合并左右数组
        left, right = lo, mid + 1
        p = lo

        while p <= hi:
            if left > mid:
                arr[p] = self.temp_arr[right]
                right += 1
            elif right > hi:
                arr[p] = self.temp_arr[left]
                left += 1
            elif self.temp_arr[left] > self.temp_arr[right]:
                arr[p] = self.temp_arr[right]
                right += 1
            else:
                arr[p] = self.temp_arr[left]
                left += 1
            p += 1
