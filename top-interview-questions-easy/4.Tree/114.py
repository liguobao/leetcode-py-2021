# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from b_tree import BinaryTree


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        stack_node = [root]
        prev_node = None
        while stack_node:
            current_node = stack_node.pop()
            if prev_node:
                prev_node.left = None
                prev_node.right = current_node
            if current_node.right:
                stack_node.append(current_node.right)
            if current_node.left:
                stack_node.append(current_node.left)
            prev_node = current_node


tree_array = [3, 9, 20, None, None, 15, 7]
print(f"tree_array:{tree_array}")
b_tree = BinaryTree(tree_array)
Solution().flatten(b_tree.root)
print(f"result:{b_tree}")
