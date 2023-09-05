#
# @lc app=leetcode.cn id=261 lang=python3
#
# [261] Graph Valid Tree
#

# @lc code=start
from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UF(n)

        for edge in edges:
            if uf.connected(*edge):
                return False
            uf.union(*edge)

        return uf.count == 1


class UF:
    def __init__(self, n: int) -> None:
        self.parent = [i for i in range(n)]
        self.count = n

    def union(self, a: int, b: int) -> None:
        root_a, root_b = self.find_root(a), self.find_root(b)
        if root_a == root_b:
            return
        self.parent[root_a] = root_b
        self.count -= 1

    def find_root(self, a: int) -> int:
        if self.parent[a] != a:
            self.parent[a] = self.find_root(self.parent[a])
        return self.parent[a]

    def connected(self, a: int, b: int) -> bool:
        return self.find_root(a) == self.find_root(b)
# @lc code=end
