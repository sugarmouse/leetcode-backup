#
# @lc app=leetcode.cn id=410 lang=python3
#
# [410] 分割数组的最大值
#
from typing import List
# @lc code=start
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left, right = sum(nums) // k, sum(nums)
        res = -1

        while left <= right:
            mid = (left+right) // 2
            if self.check(nums, k, mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return res

    def check(self, nums: List[int], k: int, max_sum: int) -> bool:
        """
        The function checks if it is possible to divide a list of numbers into k subarrays such that the sum
        of each subarray is less than or equal to a given maximum sum.
        """
        check_k = 0
        tmp_sum = 0
        for num in nums:
            tmp_sum += num
            # 当存在某个元素大于最大和的时候，直接返回 False
            if num > max_sum:
                return False
            if tmp_sum >= max_sum:
                check_k += 1
                tmp_sum = 0 if tmp_sum == max_sum else num

        if tmp_sum != 0:
            check_k += 1

        return True if check_k <= k else False


# @lc code=end

# tags: 二分查找