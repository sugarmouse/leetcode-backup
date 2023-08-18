#
# @lc app=leetcode.cn id=870 lang=python3
#
# [870] 优势洗牌
#

# @lc code=start
from typing import List, Tuple
import heapq

class MaxHeapElement:
    def __init__(self, val:Tuple[int, int]):
        self.val = val

    def __lt__(self, other:'MaxHeapElement'):
        return self.val > other.val

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sz = len(nums1)

        pq = []
        for index,val in enumerate(nums2):
            heapq.heappush(pq, MaxHeapElement(val=(val, index)))

        nums1.sort()
        res = [0 for _ in range(sz)]
        left, right = 0, sz -1

        while pq:
            max_val, index = heapq.heappop(pq).val
            
            if nums1[right] > max_val:
                res[index] = nums1[right]
                right -= 1
            else:
                res[index] = nums1[left]
                left += 1
            
        return res


# @lc code=end

# 田忌赛马
# tags: 优先级队列