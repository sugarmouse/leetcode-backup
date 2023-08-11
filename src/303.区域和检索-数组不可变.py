#
# @lc app=leetcode.cn id=303 lang=python3
#
# [303] 区域和检索 - 数组不可变
#

from typing import List

# @lc code=start


class NumArray:
    def __init__(self, nums: List[int]):
        self.preSum: List[int] = []
        sum = 0
        for num in nums:
            sum += num
            self.preSum.append(sum)
        print(self.preSum)

    def sumRange(self, left: int, right: int) -> int:
        return self.preSum[right] - (self.preSum[left - 1] if left != 0 else 0)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end
