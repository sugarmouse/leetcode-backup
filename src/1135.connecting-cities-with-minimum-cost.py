#
# @lc app=leetcode.cn id=1135 lang=python3
#
# [1135] Connecting Cities With Minimum Cost
#

# @lc code=start
from typing import List


class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        connections.sort(key=lambda item: item[2])
        uf = UF(n)
        res = 0
        for connect in connections:
            [a, b, cost] = connect
            if not uf.connected(a, b):
                uf.union(a, b)
                res += cost

        return -1 if uf.count != 1 else res


class UF:
    def __init__(self, n: int) -> None:
        self.parent = [i for i in range(n+1)]
        self.count = n

    def union(self, a: int, b: int):
        root_a, root_b = self.find_root(a), self.find_root(b)
        if root_a == root_b:
            return

        self.parent[root_b] = root_a
        self.count -= 1

    def find_root(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find_root(self.parent[x])
        return self.parent[x]

    def connected(self, a: int, b: int) -> bool:
        return self.find_root(a) == self.find_root(b)

# @lc code=end
