#
# @lc app=leetcode.cn id=528 lang=python3
#
# [528] 按权重随机选择
#
# @lc code=start
import random


class Solution:

    def __init__(self, w: List[int]):
        self.sz = len(w)
        self.pre_sum = [0 if i != 0 else w[0] for i in range(self.sz)]

        for i in range(1, self.sz):
            self.pre_sum[i] = w[i] + self.pre_sum[i-1]

    def pickIndex(self) -> int:
        rand_num = random.random() * self.pre_sum[self.sz - 1]

        left, right = 0, self.sz

        while left <= right:
            mid = (left + right) // 2

            if self.pre_sum[mid] == rand_num:
                right = mid - 1
            elif self.pre_sum[mid] > rand_num:
                right = mid - 1
            else:
                left = mid + 1

        return right + 1


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# @lc code=end
