#
# @lc app=leetcode.cn id=1631 lang=python3
#
# [1631] Path With Minimum Effort
#

# @lc code=start
from typing import List
from heapq import heappush, heappop


class NodeCost:
    def __init__(self, node: int, cost: int) -> None:
        self.node = node
        self.cost = cost

    def __lt__(self, other: 'NodeCost') -> bool:
        return self.cost < other.cost

# Dijkstra 最短路径
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row = len(heights)
        col = len(heights[0])
        graph = self.buidGraph(heights, row, col)
        costs = [None] * (row * col)
        pq: List[NodeCost] = []

        # 问题转换为 graph[0] 到 graph[col*row] 的最有路径
        costs[0] = 0
        heappush(pq, NodeCost(0, 0))

        while pq:

            cur = heappop(pq)
            cur_node, cur_cost = cur.node, cur.cost
            if costs[cur_node] is not None and costs[cur_node] < cur_cost:
                continue

            for adj in graph[cur_node]:
                adj_node, adj_cost_c = adj.node, adj.cost

                adj_cost_s = max(costs[cur_node], adj_cost_c)

                if costs[adj_node] is None or adj_cost_s < costs[adj_node]:
                    costs[adj_node] = adj_cost_s
                    heappush(pq, NodeCost(adj_node, adj_cost_s))

        return costs[col*row - 1]

    def buidGraph(self, heights: List[List[int]], row: int, col: int) -> List[List[NodeCost]]:
        graph = [[] for _ in range(row * col)]

        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        for i in range(row):
            for j in range(col):
                neighbor = graph[i*col + j]
                for dir in dirs:
                    nx = i + dir[0]
                    ny = j + dir[1]
                    # 越界跳过
                    if nx >= row or nx < 0 or ny >= col or ny < 0:
                        continue
                    neighbor.append(NodeCost(nx*col + ny, abs(heights[i][j] - heights[nx][ny])))

        return graph

# @lc code=end

# 并查集
# 可以想象成初始状态就是 m*n 个点，把每条无向边按照权重由低到高一个个连接起来
# 当正好连接一条边时满足 0,0 和 n-1,m-1 联通，那么这条边的权重就是连接两点的最低 cost
class Solution2:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        edges = []
        m = len(heights)
        n = len(heights[0])

        for i in range(m):
            for j in range(n):
                c = i*n + j
                if i > 0:
                    # 推入上节点和当前节点组成的边
                    u = c - n
                    w = abs(heights[i][j] - heights[i-1][j])
                    edges.append([u,c,w])
                if j > 0:
                    # 推入左节点和当前节点组成的边
                    l = c - 1
                    w = abs(heights[i][j] - heights[i][j-1])
                    edges.append([l,c,w])

        edges.sort(key= lambda e: e[2])

        ans = 0
        uf = UF(m*n)
        for a,b,w in edges:
            uf.union(a,b)
            if uf.connected(0, m*n -1):
                ans =  w
                break
        return ans


class UF:
    def __init__(self, n:int):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
    
    def union(self, a:int, b:int) -> bool:
        root_a = self.find_root(a)
        root_b = self.find_root(b)
        if root_a == root_b:
            return False
        
        if self.size[root_a] < self.size[root_b]:
            root_a, root_b = root_b, root_a

        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b]
        return True
    
    def find_root(self, a:int) -> int:
        if self.parent[a] != a:
            self.parent[a] = self.find_root(self.parent[a])
        return self.parent[a]

    def connected(self, a:int, b:int) -> bool:
        return self.find_root(a) == self.find_root(b)
    