#
# @lc app=leetcode.cn id=304 lang=python3
#
# [304] 二维区域和检索 - 矩阵不可变
#
from typing import List
# @lc code=start


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix[0]) + 1
        n = len(matrix) + 1
        self.preSum: List[List[int]] = [[0] * m for _ in range(n)]

        for i, list in enumerate(matrix):
            for j, num in enumerate(list):
                self.preSum[i+1][j+1] = num + self.preSum[i][j+1] + \
                    self.preSum[i+1][j] - self.preSum[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.preSum[row2+1][col2 + 1] - self.preSum[row1][col2 + 1] \
            - self.preSum[row2+1][col1] + self.preSum[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end

# 没有用守卫，主打一个写的不是给人看的代码


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.preSum: List[List[int]] = [
            [0] * len(matrix[0]) for _ in range(len(matrix))]

        for row, list in enumerate(matrix):
            for col, num in enumerate(list):
                self.preSum[row][col] = num \
                    + (self.preSum[row][col - 1] if col != 0 else 0) \
                    + (self.preSum[row - 1][col] if row != 0 else 0) \
                    - (self.preSum[row - 1][col-1] if (row != 0 and col != 0) else 0)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.preSum[row2][col2] \
            - (self.preSum[row1 - 1][col2] if row1 != 0 else 0) \
            - (self.preSum[row2][col1 - 1] if col1 != 0 else 0) \
            + (self.preSum[row1 - 1][col1 - 1] if (col1 != 0 and row1 != 0) else 0)
