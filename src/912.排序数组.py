#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#

# @lc code=start
class Solution:
    def __init__(self):
        self.temp_arr = []

    def sortArray(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        self.temp_arr = [0 for _ in range(nums_len)]
        self.sortArrayBetween(nums, 0, nums_len - 1)
        return nums

    def sortArrayBetween(self, nums: List[int], left: int, right: int) -> None:
        if left >= right:
            return

        mid = (left + right) // 2
        self.sortArrayBetween(nums, left, mid)
        self.sortArrayBetween(nums, mid + 1, right)

        self.merge(nums, left, mid, right)

    def merge(self, nums: List[int], left: int, mid: int, right: int):

        for index in range(left, right + 1):
            self.temp_arr[index] = nums[index]

        i, j = left, mid + 1

        p = left

        while p <= right:
            if i > mid or j > right:
                # 某一半数组元素已经用完
                if i <= mid:
                    nums[p] = self.temp_arr[i]
                    i += 1
                if j <= right:
                    nums[p] = self.temp_arr[j]
                    j += 1
            elif self.temp_arr[i] <= self.temp_arr[j]:
                nums[p] = self.temp_arr[i]
                i += 1
            else:
                nums[p] = self.temp_arr[j]
                j += 1

            p += 1


# @lc code=end
