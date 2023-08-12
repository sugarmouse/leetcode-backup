#
# @lc app=leetcode.cn id=1109 lang=python3
#
# [1109] 航班预订统计
#

# @lc code=start
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0 for _ in range(n)]

        # 初始化 diff 数组
        for booking in bookings:
            [first, last, seat] = booking
            diff[first-1] += seat
            if last < n:
                diff[last] -= seat

        # 还原原数组
        for i in range(1, n):
            diff[i] = diff[i] + diff[i-1]
        return diff

# @lc code=end

# tags: 差分数组
