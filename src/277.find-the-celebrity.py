#
# @lc app=leetcode.cn id=277 lang=python3
#
# [277] Find the Celebrity
#

# @lc code=start
# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

# 找出最大 indegree 为 n-1, 且 outdegree 为 0 的节点，返回该节点
# 如果不存在，则返回 -1

# celebrity 不可能认识其他人，所以当 knows(a,b) == True 时，a 就已经不可能是 celebrity 了

# 同 Solution2，节省空间版
class Solution:
    def findCelebrity(self, n: int) -> int:
        if n == 1:
            return 0

        p, q = 0, 1

        while p < n and q < n:
            if knows(p, q) or not knows(q, p):
                # 肯定排除 p
                p += 1
                if p == q:
                    p += 1
            else:
                q += 1
                if q == p:
                    q += 1

        cand = min(p, q)
        for other in range(n):
            if other == cand:
                continue
            if knows(cand, other) or not knows(other, cand):
                return -1

        return cand

# @lc code=end

# 如果 celebrity 存咋说的话，只可能有一个
# 所以可以取两个，根据两者关系排除一个
# 一次排除之后，只剩下一个，再检查最后剩下的一个是否满足要求
class Solution2:
    def findCelebrity(self, n: int) -> int:
        q = [i for i in range(n)]

        while len(q) >= 2:
            p1, p2 = q[0], q[1]
            if knows(p1, p2) or not knows(p2, p1):
                # 肯定排除 p1
                q.pop(0)
            else:
                # 排除 p2
                q.pop(1)

        cand = q[0]
        for other in range(n):
            if other == cand:
                continue
            if knows(cand, other) or not knows(other, cand):
                return -1

        return cand


# 暴力解法
class Solution1:
    def findCelebrity(self, n: int) -> int:
        for cand in range(n):
            other = 0
            while other < n:
                if cand == other:
                    # 自己碰到自己
                    other += 1
                    continue
                if knows(cand, other) or not knows(other, cand):
                    # 当前 cand 不是 celebrity
                    break
                other += 1
            if other == n:
                return cand
        return -1
