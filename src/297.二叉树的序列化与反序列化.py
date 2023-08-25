#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 层序遍历解法
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        q = [root]
        res = ''

        while q:
            cur_level_size = len(q)
            
            # 遍历当前层的节点
            for _ in range(cur_level_size):
                cur_node = q.pop(0)

                if cur_node is None:
                    res += '#,'
                    continue
                res += f'{cur_node.val},'
                q.extend([cur_node.left, cur_node.right])
        return res[:-1]
        

    def deserialize(self, data: str):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        data_list = data.split(',')

        # 生成 root 节点
        root_val = data_list.pop(0)
        if root_val == '#':
            return None
        root = TreeNode(int(root_val))

        q = [root]

        while data_list:

            cur_level_size = len(q)
            
            # 对当前层节点生成左右子节点 
            for _ in range(cur_level_size):

                cur_node = q.pop(0)

                left_val = data_list.pop(0)
                if left_val == '#':
                    cur_node.left = None
                else:
                    cur_node.left = TreeNode(int(left_val))
                    q.append(cur_node.left)
                
                right_val = data_list.pop(0)
                if right_val == '#':
                    cur_node.right = None
                else:
                    cur_node.right = TreeNode(int(right_val))
                    q.append(cur_node.right)
        
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end



# 前序遍历解法
class Codec2:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return '#'
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        r = f'{root.val},{left},{right}'
        return r

    def deserialize(self, data: str):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data_list = data.split(',')
        return self.build(data_list)

    def build(self, data: List[str]) -> Optional[TreeNode]:
        if not data:
            return None

        cur_node_str = data.pop(0)

        if cur_node_str == '#':
            return None

        root = TreeNode(int(cur_node_str))

        root.left = self.build(data)
        root.right = self.build(data)

        return root


# 后序遍历解法
# 和前序遍历方法类似，不过反序列化时先右后左
class Codec3:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return '#'
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        r = f'{left},{right},{root.val}'
        return r

    def deserialize(self, data: str):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data_list = data.split(',')
        return self.build(data_list)

    def build(self, data: List[str]) -> Optional[TreeNode]:
        if not data:
            return None

        root_val = data.pop()

        if root_val == '#':
            return None

        root = TreeNode(root_val)

        root.right = self.build(data)
        root.left = self.build(data)

        return root