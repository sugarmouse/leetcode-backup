#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start

# 矩阵顺时针旋转 90 度
#   先沿对称轴镜像
#   然后逐行翻转
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for row, arr in enumerate(matrix):
            for col, num in enumerate(arr):
                if row < col:
                    matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        for row, arr in enumerate(matrix):
            i, j = 0, len(arr) - 1
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

# @lc code=end

