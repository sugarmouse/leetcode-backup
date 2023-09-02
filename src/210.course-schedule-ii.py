#
# @lc app=leetcode.cn id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
from typing import List
from collections import deque


# 拓扑排序
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = self.buildGraph(numCourses, prerequisites)

        # 初始化 0 indegree 节点队列
        indegree = [0 for _ in range(numCourses)]
        q = deque()
        for edge in prerequisites:
            indegree[edge[0]] += 1
        for i, v in enumerate(indegree):
            if v == 0:
                q.append(i)

        # 从 0 indegree 节点逐个遍历
        res = []
        count = 0
        while q:
            cur = q.popleft()
            count += 1
            res.append(cur)

            for next_node in graph[cur]:
                indegree[next_node] -= 1
                if indegree[next_node] == 0:
                    q.append(next_node)

        # 检测是否有环，返回结果
        return res if count == numCourses else []

    def buildGraph(self, numCourses: int, prerequisites: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(numCourses)]

        for edge in prerequisites:
            graph[edge[1]].append(edge[0])

        return graph


# @lc code=end

# DFS
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
