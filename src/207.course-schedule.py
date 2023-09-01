#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
from typing import List

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
# @lc code=end
