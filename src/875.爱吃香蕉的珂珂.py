#
# @lc app=leetcode.cn id=875 lang=python3
#
# [875] 爱吃香蕉的珂珂
#
from typing import List
# @lc code=start
class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        right = max(piles)
        left = 1

        while left <= right:
            mid = left + (right - left) // 2

            time = self.needed_time(piles, h, mid)

            if time == h:
                right = mid - 1
            elif time < h:
                right = mid -1
            else:
                left = mid + 1

        return right + 1


    def needed_time(self, piles: List[int], h: int, s: int) -> int:
        a = 0

        for p in piles:
            a += p // s
            if p % s != 0:
                a += 1
        return a
# @lc code=end

# tags: 二分查找