#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        left, right = 0, n-1
        up, low = 0, n - 1
        num = 1

        while num <= n * n:
            if up <= low:
                for i in range(left, right + 1):
                    matrix[up][i] = num
                    num += 1
                up += 1

            if left <= right:
                for j in range(up, low + 1):
                    matrix[j][right] = num
                    num += 1
                right -= 1

            if up <= low:
                for k in range(right, left - 1,  -1):
                    matrix[low][k] = num
                    num += 1
                low -= 1

            if left <= right:
                for l in range(low, up - 1, -1):
                    matrix[l][left] = num
                    num += 1
                left += 1

        return matrix


# @lc code=end
