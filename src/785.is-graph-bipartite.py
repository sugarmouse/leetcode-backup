#
# @lc app=leetcode.cn id=785 lang=python3
#
# [785] Is Graph Bipartite?
#

# @lc code=start
from typing import List
from collections import deque


class Solution:
    # 二分图，双色问题，BFS
    def isBipartite(self, graph: List[List[int]]) -> bool:
        sz = len(graph)
        self.isBi = True
        self.color = [False] * sz
        self.visited = [False] * sz

        for i in range(sz):
            if not self.visited[i]:
                self.traverse(graph, i)
        
        return self.isBi

    def traverse(self, graph: List[List[int]], node: int):
        q = deque()
        q.append(node)
        self.visited[node] = True

        while q and self.isBi:
            cur = q.popleft()
            for next_node in graph[cur]:
                if not self.visited[next_node]:
                    # 相邻节点还没有遍历过
                    self.color[next_node] = not self.color[cur]
                    self.visited[next_node] = True
                    q.append(next_node)
                else:
                    # 相邻节已经遍历过，检查
                    if self.color[next_node] == self.color[cur]:
                        self.isBi = False
                        return


# @lc code=end

class Solution1:
    # 二分图，双色问题，DFS
    def isBipartite(self, graph: List[List[int]]) -> bool:
        self.isBi = True
        sz = len(graph)
        self.colors = [False] * sz
        visited = [False for _ in range(sz)]

        for i in range(sz):
            if not visited[i]:
                self.traverse(graph, visited, i)
                if not self.isBi:
                    break
        return self.isBi

    def traverse(self, graph: List[List[int]], visited: List[bool], node: int):
        if not self.isBi:
            return

        visited[node] = True

        for neighbor in graph[node]:
            # 因为需要知道当前节点和相邻节点的关系，所以把 base case 放到 for loop 里面
            if not visited[neighbor]:
                self.colors[neighbor] = not self.colors[node]
                self.traverse(graph, visited, neighbor)
            else:
                # check color if differ from cur node
                if self.colors[neighbor] == self.colors[node]:
                    self.isBi = False
                    return
