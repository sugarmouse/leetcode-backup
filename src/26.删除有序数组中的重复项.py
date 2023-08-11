#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        left, right = 0, 0

        while right < len(nums):
            nums[left] = nums[right]

            while right < len(nums) and nums[right] == nums[left]:
                right += 1
            left += 1
        return left


# @lc code=end
