#
# @lc app=leetcode.cn id=990 lang=python3
#
# [990] Satisfiability of Equality Equations
#

# @lc code=start
from typing import List



class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UF(26)

        # 先联通所有的 ==
        for eq in equations:
            if eq[1] == '=':
                x = ord(eq[0]) - ord('a')
                y = ord(eq[3]) - ord('a')
                uf.union(x, y)

        # 检查所有的 != 是否满足要求
        for eq in equations:
            if eq[1] == '!':
                x, y = self.getIndex(eq)
                if uf.connected(x, y):
                    return False

        return True

    def getIndex(self, eq: str) -> (int, int):
        x = ord(eq[0]) - ord('a')
        y = ord(eq[3]) - ord('a')
        return x, y


class UF:
    def __init__(self, n: int) -> None:
        self.parent = [i for i in range(n)]
        self.count = n

    def union(self, a: int, b: int):
        rootA, rootB = self.find_root(a), self.find_root(b)
        if rootA == rootB:
            return
        self.parent[rootA] = rootB
        self.count -= 1

    def find_root(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find_root(self.parent[x])
        return self.parent[x]

    def connected(self, a: int, b: int) -> bool:
        return self.find_root(a) == self.find_root(b)

    def count(self) -> int:
        return self.count

# tags: 并查集

# @lc code=end
