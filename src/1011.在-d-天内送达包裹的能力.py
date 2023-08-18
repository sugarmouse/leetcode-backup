#
# @lc app=leetcode.cn id=1011 lang=python3
#
# [1011] 在 D 天内送达包裹的能力
#
from typing import List
# @lc code=start


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)

        while left <= right:
            mid = (left + right) // 2
            day = self.needed_day(weights, mid)
            if day == days:
                right = mid - 1
            elif day > days:
                left = mid + 1
            else:
                right = mid - 1
        return right + 1
            

    def needed_day(self, weights: List[int], capacity: int) -> int:
        day = 0
        tmp_sum = 0

        for weight in weights:
            tmp_sum += weight
            if tmp_sum >= capacity:
                day += 1
                tmp_sum = 0 if tmp_sum == capacity else weight
        return day if tmp_sum == 0 else day + 1


# @lc code=end
