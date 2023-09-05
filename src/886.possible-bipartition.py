#
# @lc app=leetcode.cn id=886 lang=python3
#
# [886] Possible Bipartition
#

# @lc code=start
from typing import List
from collections import deque

# 二分图检测，双色问题
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = self.buildGraph(n, dislikes)
        self.visited = [False] * (n+1)
        self.color = [False] * (n+1)
        self.isBi = True

        for i in range(1, n+1):
            if not self.visited[i] and self.isBi:
                self.bfs(graph, i)

        return self.isBi

    def bfs(self, graph: List[List[int]], node: int):
        q = deque()
        q.append(node)

        while q and self.isBi:
            cur = q.popleft()
            self.visited[cur] = True

            for next_node in graph[cur]:
                if self.visited[next_node]:
                    # 下一个节点已经遍历过
                    if self.color[cur] == self.color[next_node]:
                        self.isBi = False
                        return
                else:
                    # 下一个节点还没有遍历过
                    self.color[next_node] = not self.color[cur]
                    q.append(next_node)

    def buildGraph(self, n: int, dislikes: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n+1)]

        for edge in dislikes:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        return graph

# @lc code=end
