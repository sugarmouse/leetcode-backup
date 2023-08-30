#
# @lc app=leetcode.cn id=1650 lang=python3
#
# [1650] Lowest Common Ancestor of a Binary Tree III
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        ptr_p, ptr_q = p, q

        while ptr_p != ptr_q:

            ptr_p = ptr_p.parent
            if ptr_p is None:
                ptr_p = q

            ptr_q = ptr_q.parent
            if ptr_q is None:
                ptr_q = p
        
        return ptr_p
        
        
# @lc code=end

