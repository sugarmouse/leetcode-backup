#
# @lc app=leetcode.cn id=743 lang=python3
#
# [743] Network Delay Time
#

# @lc code=start
from heapq import heappush, heappop
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = self.buildGraph(times, n)
        distTo = [None] * (n+1)
        pq: List[NodeState] = []

        distTo[k] = 0
        heappush(pq, NodeState(k, 0))

        while pq:

            cur = heappop(pq)
            curNodeId, curDist = cur.node, cur.dist

            if distTo[curNodeId] and curDist > distTo[curNodeId]:
                continue

            for nextNode in graph[curNodeId]:
                [nextNodeId, distFromCurToNext] = nextNode
                distFromStartToNExt = distTo[curNodeId] + distFromCurToNext

                if distTo[nextNodeId] is None or distTo[nextNodeId] > distFromStartToNExt:
                    distTo[nextNodeId] = distFromStartToNExt
                    heappush(pq, NodeState(nextNodeId, distFromStartToNExt))

        return -1 if not self.allConnected(distTo) else max(distTo)

    def allConnected(self, distTo: List[int]):
        distTo.pop(0)
        for dist in distTo:
            if dist is None:
                return False
        return True

    def buildGraph(self, times: List[List[int]], n) -> List[List[int]]:
        graph = [[] for _ in range(n + 1)]
        for time in times:
            [f, t, d] = time
            graph[f].append([t, d])
        return graph


# NodeState class 记录节点 id 和从起点到 id 节点的距离
class NodeState:
    def __init__(self, node: int, dist: int):
        self.node = node
        self.dist = dist

    def __lt__(self, other: 'NodeState') -> bool:
        return self.dist < other.dist
# @lc code=end

# Dijkstra 算法