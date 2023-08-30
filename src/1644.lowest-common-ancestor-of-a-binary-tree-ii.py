# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 找 p，q 的公共祖先，p，q 有可能不在树中
# 所以要在后序遍历的位置匹配节点，遍历每一个节点
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.foundP, self.foundQ = False, False
        node = self.find(root, p, q)
        if not self.foundP or not self.foundQ:
            return None
        return node

    
    def find(self, node:'TreeNode', p:'TreeNode', q:'Treenode') -> bool:
        if not node:
            return None

        left = self.find(node.left, p, q)
        right = self.find(node.right, p, q)

        # 左右都找到了一个节点，说明当前节点就是 LCA 节点
        if left and right:
            return node

        # 节点匹配并且做标记
        if node is p or node is q:
            if node is p:
                self.foundP = True
            if node is q:
                self.foundQ = True
            return node

        # 向上传递找到的节点
        return left if left else right