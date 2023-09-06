#
# @lc app=leetcode.cn id=1514 lang=python3
#
# [1514] Path with Maximum Probability
#

# @lc code=start
from typing import List
from heapq import heappush, heappop


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = self.buildGraph(n, edges, succProb)

        pq: List[NodeProb] = []
        probs = [None] * n

        probs[start_node] = 1
        heappush(pq, NodeProb(start_node, 1))

        while pq:
            cur = heappop(pq)
            curNode, curProb = cur.node, cur.prob
            if probs[curNode] is not None and probs[curNode] > curProb:
                continue

            for nextNode in graph[curNode]:
                nextNodeId, prob = nextNode
                nextProb = prob * probs[cur.node]

                if probs[nextNodeId] is None or probs[nextNodeId] < nextProb:
                    probs[nextNodeId] = nextProb
                    heappush(pq, NodeProb(nextNodeId, nextProb))

        return probs[end_node] if probs[end_node] is not None else 0.00000

    def buildGraph(self, n: int, edges: List[List[int]], succProb: List[float]) -> List[List[tuple[int, float]]]:
        graph: List[List[tuple[int, int, float]]] = [[] for _ in range(n)]

        for i in range(len(edges)):
            edge = edges[i]
            p = succProb[i]
            graph[edge[0]].append(tuple((edge[1], p)))
            graph[edge[1]].append(tuple((edge[0], p)))
        return graph


class NodeProb:
    def __init__(self, node: int, prop: float) -> None:
        self.node = node
        self.prob = prop

    def __lt__(self, other: 'NodeProb') -> bool:
        return self.prob > other.prob

# @lc code=end
