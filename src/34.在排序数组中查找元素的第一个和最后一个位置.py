#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
from typing import List

# @lc code=start


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.bound(nums, target, is_left=True), self.bound(nums, target, is_right=True)]

    def bound(self, nums: List[int], t: int, is_left: bool = False, is_right: bool = False) -> int:
        left, right = 0, len(nums) - 1
        result = -1
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == t:
                result = mid
                if is_left:
                    right = mid - 1
                if is_right:
                    left = mid + 1
            elif nums[mid] < t:
                left = mid + 1
            elif nums[mid] > t:
                right = mid - 1
        return result

# @lc code=end
