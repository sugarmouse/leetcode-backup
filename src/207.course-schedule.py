#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.hasCycle = False
        graph = self.buildGraph(numCourses, prerequisites)
        visited = [False for _ in range(numCourses)]
        path = [False for _ in range(numCourses)]

        for i in range(numCourses):
            self.traverse(graph, i, visited, path)

        return False if self.hasCycle else True

    def traverse(self, graph: List[List[int]], node: int, visited: List[bool], path: List[bool]):
        if path[node]:
            self.hasCycle = True
        if visited[node] or self.hasCycle:
            return

        visited[node] = True
        path[node] = True
        for t in graph[node]:
            self.traverse(graph, t, visited, path)

        path[node] = False

    # 邻接表建树
    def buildGraph(self, numCourses: int, prerequisites: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(numCourses)]

        for edge in prerequisites:
            [a, b] = edge
            graph[a].append(b)

        return graph
# @lc code=end
