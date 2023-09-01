#
# @lc app=leetcode.cn id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
from typing import List

# 拓扑排序


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.path = [False for _ in range(numCourses)]
        self.visited = [False for _ in range(numCourses)]
        self.hasCycle = False
        self.postorder = []

        graph = self.buildGraph(numCourses, prerequisites)

        for i in range(numCourses):
            self.traverse(graph, i)

        if self.hasCycle:
            return []

        self.postorder.reverse()
        return self.postorder

    def traverse(self, graph: List[List[int]], node: int):
        if self.path[node]:
            self.hasCycle = True

        if self.visited[node] or self.hasCycle:
            return

        self.path[node] = True
        self.visited[node] = True
        for t in graph[node]:
            self.traverse(graph, t)
        # 记录后序遍历结果
        self.postorder.append(node)
        self.path[node] = False

    def buildGraph(self, numCourses: int, prerequisites: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(numCourses)]

        for edge in prerequisites:
            graph[edge[1]].append(edge[0])

        return graph


# @lc code=end
