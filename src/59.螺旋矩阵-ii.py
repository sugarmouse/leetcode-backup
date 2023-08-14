#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        upper_bound, lower_bound = 0, n - 1
        left_bound, right_bound = 0, n - 1
        # 需要填入矩阵的数字
        num = 1
        
        while num <= n * n:
            if upper_bound <= lower_bound:
                # 在顶部从左向右遍历
                for j in range(left_bound, right_bound+1):
                    matrix[upper_bound][j] = num
                    num += 1
                # 上边界下移
                upper_bound += 1
            
            if left_bound <= right_bound:
                # 在右侧从上向下遍历
                for i in range(upper_bound, lower_bound+1):
                    matrix[i][right_bound] = num
                    num += 1
                # 右边界左移
                right_bound -= 1
            
            if upper_bound <= lower_bound:
                # 在底部从右向左遍历
                for j in range(right_bound, left_bound-1, -1):
                    matrix[lower_bound][j] = num
                    num += 1
                # 下边界上移
                lower_bound -= 1
            
            if left_bound <= right_bound:
                # 在左侧从下向上遍历
                for i in range(lower_bound, upper_bound-1, -1):
                    matrix[i][left_bound] = num
                    num += 1
                # 左边界右移
                left_bound += 1
        
        return matrix

# @lc code=end
