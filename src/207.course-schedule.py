#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
from typing import List
from collections import deque

# BFS
# 通过课程依赖关系，建图
# 遍历图，检测是否有环
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = self.buildGraph(numCourses, prerequisites)

        # 找到图中入度为 0 的所有节点，构成队列
        q = deque()
        # 记录每个节点的入度
        indegree = [0 for _ in range(numCourses)]
        for edge in prerequisites:
            [dep, want] = edge
            indegree[dep] += 1
        
        for index, val in enumerate(indegree):
            if val == 0:
                q.append(index)

        # 从队列中不断弹出节点
        # 相当于从图中不断删除入度为 0 的节点
        count = 0
        while q:
            # 当前节点入度为 0 ，此节点不可能在环中，所以可以直接弹出
            # 并且更新记数
            cur = q.popleft()
            count += 1
            # 当前节点被从图中拿走，那么他指向的节点入度都要减一
            for next_node in graph[cur]:
                indegree[next_node] -= 1
                # 如果当前节点也成为了入度为 0 的节点，那么推入队列继续以上操作
                if indegree[next_node] == 0:
                    q.append(next_node)

        # 如果图中有环，那么环中的节点不会再删除节点的操作中成为入度为 0 的节点
        # 所以最后遍历到的节点数字 count = numCourses - 成环的节点数
        # 如果 count == numsCourses，那么成环节点数为 0
        return count == numCourses

    # 邻接表建树
    def buildGraph(self, numCourses: int, prerequisites: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(numCourses)]
        # prerequisites 数组里存的其实是课程与课程直接的边
        for edge in prerequisites:
            [dep, want] = edge
            graph[want].append(dep)
        return graph
# @lc code=end

# DFS
# 通过课程依赖关系，建图
# 遍历图，检测是否有环
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.hasCycle = False
        graph = self.buildGraph(numCourses, prerequisites)
        visited = [False for _ in range(numCourses)]
        path = [False for _ in range(numCourses)]

        # 课程所组成的图不一定都是联通的，所以需要从每个课程出发遍历一遍
        for i in range(numCourses):
            self.traverse(graph, i, visited, path)

        return False if self.hasCycle else True

    def traverse(self, graph: List[List[int]], node: int, visited: List[bool], path: List[bool]):
        if path[node]:
            self.hasCycle = True
        
        if visited[node] or self.hasCycle:
            return

        visited[node] = True
        # 遍历路径经过该节点，把该节点加入路径
        path[node] = True
        for t in graph[node]:
            self.traverse(graph, t, visited, path)
        # 当前节点遍历结束，从路径上去除
        path[node] = False

    # 邻接表建树
    def buildGraph(self, numCourses: int, prerequisites: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(numCourses)]
        # prerequisites 数组里存的其实是课程与课程直接的边
        for edge in prerequisites:
            [a, b] = edge
            graph[a].append(b)
        return graph