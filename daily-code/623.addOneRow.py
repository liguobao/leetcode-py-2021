# Definition for a binary tree node.
from b_tree import BinaryTree


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def addOneRow(self, root, val, depth):
        """
        :type root: TreeNode
        :type val: int
        :type depth: int
        :rtype: TreeNode
        """
        if depth == 1:
            return TreeNode(val, root, None)
        stack_node = [root]
        # 层次遍历，所有节点按层存储到数据
        level_array = []
        while stack_node:
            stack_len = len(stack_node)
            level_nodes = []
            while stack_len > 0:
                current_node = stack_node[0]
                stack_node.remove(current_node)
                level_nodes.append(current_node)
                if current_node.left:
                    stack_node.append(current_node.left)
                if current_node.right:
                    stack_node.append(current_node.right)
                stack_len = stack_len - 1
            level_array.append(level_nodes)
        # 找到需要处理的那一行
        for node in level_array[depth-2]:
            node.left = TreeNode(val, node.left, None)
            node.right = TreeNode(val, None, node.right)
        return root


root = [4, 2, 6, 3, 1, 5]
val = 1
depth = 2

tree_node = BinaryTree(root)
result = Solution().addOneRow(tree_node.root, val, depth)
print(result)
