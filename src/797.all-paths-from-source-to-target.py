#
# @lc app=leetcode.cn id=797 lang=python3
#
# [797] All Paths From Source to Target
#

# @lc code=start
from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.onPath = []
        self.res = []
        self.traverse(graph, 0)
        return self.res

    def traverse(self, graph: List[List[int]], node: int):
        # 将当前节点推入 path
        self.onPath.append(node)

        # 如果到达了节点 n-1，加入现在的路径
        if node == len(graph)-1:
            self.res.append(self.onPath.copy())

        # 遍历相邻节点
        for neighbor in graph[node]:
            self.traverse(graph, neighbor)

        # 当前节点遍历结束，将当前节点弹出 path
        self.onPath.pop()

# @lc code=end
