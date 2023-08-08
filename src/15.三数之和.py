#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
from typing import List
# @lc code=start


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return self.nSum(nums, 3, 0, 0)

    def nSum(self, nums: List[int], n: int, target: int, start: int) -> List[List[int]]:
        size = len(nums)
        res: List[List[int]] = []

        if n < 2 or n > size:
            return res

        if n == 2:
            lo, hi = start, size - 1

            while lo < hi:
                left, right = nums[lo], nums[hi]
                sum = left + right
                if sum == target:
                    res.append([left, right])
                    while lo < hi and nums[lo] == left:
                        lo += 1
                    while lo < hi and nums[hi] == right:
                        hi -= 1
                elif sum < target:
                    while lo < hi and nums[lo] == left:
                        lo += 1
                else:
                    while lo < hi and nums[hi] == right:
                        hi -= 1
            return res

        else:
            for i in range(start, len(nums)):
                subs = self.nSum(nums, n-1, target-nums[i], i+1)
                for arr in subs:
                    arr.append(nums[i])
                    res.append(arr)
                while i < size - 1 and nums[i] == nums[i+1]:
                    i += 1
        return res

# @lc code=end
