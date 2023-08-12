#
# @lc app=leetcode.cn id=1094 lang=python3
#
# [1094] 拼车
#
from typing import List
import heapq
# @lc code=start

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        scan_line = []
        for people_count, start, end in trips:
            scan_line.extend([[start, people_count], [end, -people_count]])
        scan_line.sort()

        max_count = 0

        for _, p in scan_line:
            max_count += p
            if max_count > capacity:
                return False
        return True

# @lc code=end

# tags: 扫描线





# 用最小堆记录离出发地的距离，以及要下车的乘客数
# 在当前出发距离时，添加乘客之前，把所有的之前需要下车的乘客先全部下车
class Solution1:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda trip: trip[1])
        heap = []
        max_count = 0
        for people_count, start, end in trips:
            heapq.heappush(heap, [end, people_count])
            # 先下后上，所以这里是 >=
            while len(heap) != 0 and start >= heap[0][0]:
                max_count -= heap[0][1]
                heapq.heappop(heap)
            max_count += people_count
            if max_count > capacity:
                return False
        return True
