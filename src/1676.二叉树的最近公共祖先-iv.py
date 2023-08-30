# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import Set

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        values = set([node.val for node in nodes])
        return self.find(root, values)
    
    def find(self, root:'TreeNode', values:Set[int]) -> 'TreeNode':
        if root is None:
            return None
        
        if root.val in values:
            return root
        
        left = self.find(root.left, values)
        right = self.find(root.right, values)

        if left and right:
            return root
        else:
            return left if left else right
