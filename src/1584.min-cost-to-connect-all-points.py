#
# @lc app=leetcode.cn id=1584 lang=python3
#
# [1584] Min Cost to Connect All Points
#

# @lc code=start
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = self.sortedWithCost(points)
        uf = UF(len(points))
        min_cost = 0

        for edge in edges:
            [a,b,cost] = edge
            if not uf.connected(a,b):
                uf.union(a,b)
                min_cost += cost
        
        return min_cost if uf.count == 1 else -1


    def sortedWithCost(self, points: List[List[int]]) -> List[List[int]]:
        n = len(points)
        res = []
        for i in range(n):
            for j in range(i+1, n):
                md = self.md(points[i], points[j])
                res.append([i, j, md])
        res.sort(key=lambda p: p[2])
        return res

    def md(self, p1: List[int], p2: List[int]) -> int:
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    

class UF:
    def __init__(self,n:int) -> None:
        self.parent = [i for i in range(n)]
        self.count = n
    
    def find(self, x:int)->int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a:int, b:int) -> None:
        r_a, r_b = self.find(a), self.find(b)   
        if r_a == r_b:
            return
        self.parent[r_a] = r_b
        self.count -= 1
    
    def connected(self, a:int, b:int) -> bool:
        return self.find(a) == self.find(b)
# @lc code=end
