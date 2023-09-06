#
# @lc app=leetcode.cn id=1135 lang=python3
#
# [1135] Connecting Cities With Minimum Cost
#

# @lc code=start
from typing import List
import heapq

# Prim 算法实现
class EdgeWrapper:
    def __init__(self, edge: List[int]) -> None:
        self.edge = edge

    def __lt__(self, other: 'EdgeWrapper') -> bool:
        return self.edge[2] < other.edge[2]


class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        self.graph = [[] for _ in range(n+1)]
        self.inMst = [False] * (n+1)
        self.pq = []
        self.weightSum = 0
        for edge in connections:
            [f,t,w] = edge
            self.graph[f].append(edge)
            self.graph[t].append([t,f,w])

        # 从节点第一个节点开始
        self.cut(1)
        self.inMst[1] = True

        while self.pq:
            [_, to, weight] = heapq.heappop(self.pq).edge
            if self.inMst[to]:
                continue
            self.weightSum += weight
            self.cut(to)
            self.inMst[to] = True

        return self.weightSum if self.allConnected() else -1

    def cut(self, n: int):
        for edge in self.graph[n]:
            to = edge[1]
            if self.inMst[to]:
                continue
            heapq.heappush(self.pq, EdgeWrapper(edge))

    def allConnected(self) -> bool:
        for index, isInMst in enumerate(self.inMst):
            if index == 0:
                continue
            if not isInMst:
                return False
        return True

# @lc code=end


# Kruskal 算法实现
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
