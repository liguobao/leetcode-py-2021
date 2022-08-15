from platform import node
from b_tree import BinaryTree

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        stack_node = [root]
        level_nodes = []
        level_nodes_nums = []
        while stack_node:
            stack_len = len(stack_node)
            current_level_nodes = []
            while stack_len > 0:
                current_node = stack_node[0]
                stack_node.remove(current_node)
                current_level_nodes.append(current_node)
                if current_node.left:
                    stack_node.append(current_node.left)
                if current_node.right:
                    stack_node.append(current_node.right)
                stack_len = stack_len - 1
            current_node_count = self.cal_current_level_node_count(
                current_level_nodes)
            level_nodes_nums.append(current_node_count)
        max_node_num = max(level_nodes_nums)
        return max_node_num

    def cal_current_level_node_count(self, current_level_nodes):
        node_count = 0
        val_list = [x.val for x in current_level_nodes]
        if -10000 not in val_list:
            return len(current_level_nodes)
        first_index = val_list.index(-10000)
        val_list.reverse()
        end_index = val_list.index(-10000)
        return len(current_level_nodes) - end_index - first_index


null = None

node_array = [1, 3, 2, 5, None]
tree = BinaryTree(node_array)
result = Solution().widthOfBinaryTree(tree.root)
print(result)


node_array = [1, 3, 2, 5, 3, null, 9]
tree = BinaryTree(node_array)
result = Solution().widthOfBinaryTree(tree.root)
print(result)


node_array = [1, 3, 2, 5, null, null, 9, 6, null, 7]
tree = BinaryTree(node_array)
result = Solution().widthOfBinaryTree(tree.root)
print(result)
