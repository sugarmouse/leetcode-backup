#
# @lc app=leetcode.cn id=327 lang=python3
#
# [327] 区间和的个数
#
from typing import List
# @lc code=start
import bisect


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        pre_sum = [0]
        for num in nums:
            pre_sum.append(pre_sum[-1] + num)

        # 离散化
        map = {}
        unique_list = sorted(list(set(pre_sum)))
        for index, val in enumerate(unique_list):
            map[val] = index + 1

        # 建树状数组，记录每个元素的个数
        bit = BIT(len(map))

        # 元素先全部加入树状数组
        for num in pre_sum:
            bit.add(map[num], 1)
        
        res = 0
        for val in pre_sum:
            # 取出元素
            bit.add(map[val], -1)
            # 确定查找范围
            left = bisect.bisect_left(unique_list, lower + val)
            right = bisect.bisect_right(unique_list, upper + val)
            res += bit.query(right) - bit.query(left)        
        return res

class BIT:
    def __init__(self, sz: int):
        self.size = sz
        self.tree = [0] * (sz + 1)

    def add(self, x: int, val: int):
        i = x
        while i <= self.size:
            self.tree[i] += val
            i += self.lowbit(i)

    def query(self, x: int) -> int:
        res = 0
        i = x
        while i > 0:
            res += self.tree[i]
            i -= self.lowbit(i)
        return res

    def lowbit(self, x: int) -> int:
        return x & -x


# @lc code=end

# 归并排序
class Solution1:
    lower = 0
    upper = 0
    count = 0
    temp = []

    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        self.lower = lower
        self.upper = upper
        self.count = 0

        sz = len(nums)
        pre_sum = [0] * (sz + 1)

        for i in range(sz):
            pre_sum[i+1] = pre_sum[i] + nums[i]

        self.merge_sort(pre_sum)
        return self.count

    def merge_sort(self, nums: List[int]):
        self.temp = [0] * len(nums)
        self.__sort(nums, 0, len(nums) - 1)

    def __sort(self, nums: List[int], lo: int, hi: int):
        if lo == hi:
            return
        mid = (lo + hi) // 2
        self.__sort(nums, lo, mid)
        self.__sort(nums, mid + 1, hi)
        self.__merge(nums, lo, mid, hi)

    def __merge(self, nums: List[int], lo: int, mid: int, hi: int):
        # 拷贝需要合并的区间内的元素
        for i in range(lo, hi+1):
            self.temp[i] = nums[i]

        # j > i, nums[j] - nums[i] 表示原数组中 arr[i]...arr[j-1] 的元素的和
        # 滑动窗口，在右边数组中维护一个窗口，在原数组中，从当前元素到窗口中的任意一个元素，都是能满足区间和的要求
        # 所以在窗口左右边界都确定的时候，窗口内的元素个数就是对于当前元素能构成的区间和的个数 [start, end)
        start = end = mid + 1
        for i in range(lo, mid + 1):
            while start <= hi and nums[start] - nums[i] < self.lower:
                start += 1
            while end <= hi and nums[end] - nums[i] <= self.upper:
                end += 1
            self.count += (end - start)

        # 合并两个已经分别排好序的数组
        i, j = lo, mid + 1
        for p in range(lo, hi+1):
            if i == mid + 1:
                nums[p] = self.temp[j]
                j += 1
            elif j == hi + 1:
                nums[p] = self.temp[i]
                i += 1
            elif self.temp[i] > self.temp[j]:
                nums[p] = self.temp[j]
                j += 1
            else:
                nums[p] = self.temp[i]
                i += 1
