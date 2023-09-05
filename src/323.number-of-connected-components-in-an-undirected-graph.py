#
# @lc app=leetcode.cn id=323 lang=python3
#
# [323] Number of Connected Components in an Undirected Graph
#
# @lc code=start
from typing import List


class Solution:
    # 并查集计算联通分量
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.parent = [i for i in range(n)]
        self.count = n
        for edge in edges:
            self.addEdge(edge)
        return self.count

    def addEdge(self, edge: List[int]) -> None:
        root1, root2 = self.find_root(edge[0]), self.find_root(edge[1])
        if root1 == root2:
            return
        self.parent[root1] = root2
        self.count -= 1

    def find_root(self, x: int) -> int:
        # 查找的过程中把路径上的节点都直接挂到 根节点 上
        if self.parent[x] != x:
            self.parent[x] = self.find_root(self.parent[x])
        return self.parent[x]
# @lc code=end
