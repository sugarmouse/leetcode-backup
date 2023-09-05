#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start
from typing import List

# 利用并查集对节点进行分类解决
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return

        m, n = len(board), len(board[0])
        # 留 m*n 作为四边的 O
        # 二维坐标 (x,y) 映射为  x*n +y
        uf = UnionFind(m*n + 1)
        dummy = m * n

        # 首列和最后一列的 'O' 和 dummy 联通
        for i in range(m):
            if board[i][0] == 'O':
                uf.union(i * n, dummy)
            if board[i][n-1] == 'O':
                uf.union(i*n + n - 1, dummy)
        # 首行和最后一行的 'O' 和 dummy 联通
        for j in range(n):
            if board[0][j] == 'O':
                uf.union(j, dummy)
            if board[m-1][j] == 'O':
                uf.union((m-1)*n + j, dummy)

        # 遍历非边缘节点，如果出现 O, 将其与其四周的所有出现的 O 联通
        d = [[1, 0], [0, 1], [0, -1], [-1, 0]]
        for i in range(1, m-1):
            for j in range(1, n-1):
                if board[i][j] == 'O':
                    for k in range(4):
                        x = i + d[k][0]
                        y = j + d[k][1]
                        if board[x][y] == 'O':
                            uf.union(x*n+y, i*n+j)

        # 遍历非边缘节点，没有和 dummy 联通的节点都变成 X
        for i in range(1, m-1):
            for j in range(1, n-1):
                if board[i][j] == 'O' and not uf.connected(dummy, i*n + j):
                    board[i][j] = 'X'


class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = [i for i in range(n)]
        self.count = n

    def union(self, a: int, b: int):
        rootA, rootB = self.find(a), self.find(b)
        if rootA == rootB:
            return
        self.parent[rootA] = rootB
        self.count -= 1

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def connected(self, a: int, b: int) -> bool:
        return self.find(a) == self.find(b)

    def count(self) -> int:
        return self.count

# @lc code=end
